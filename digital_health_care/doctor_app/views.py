from django.apps import apps
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404, JsonResponse
from django.http import HttpResponseBadRequest
from django.forms.models import model_to_dict
from django.db.models import ForeignKey

import json

from django.apps import apps

class JSONDetailView(APIView):
    model = None

    def get(self, request, pk=None, *args, **kwargs):
        if pk is not None:
            instance = self.get_instance(pk)
            data = self.serialize_instance(instance)
        else:
            queryset = self.get_queryset()
            data = [self.serialize_instance(obj) for obj in queryset]

        return Response(data)

    def get_instance(self, pk):
        try:
            return self.model.objects.get(pk=pk)
        except self.model.DoesNotExist:
            raise Http404

    def get_queryset(self):
        return self.model.objects.all()
    
    def post(self, request, *args, **kwargs):
            data = request.data
            if not isinstance(data, dict):
                return HttpResponseBadRequest("Invalid data format. Expected JSON object.")

            for field in self.model._meta.fields:
                if isinstance(field, ForeignKey) and field.name in data:
                    try:
                        related_model = field.remote_field.model
                        data[field.name] = related_model.objects.get(pk=data[field.name])
                    except related_model.DoesNotExist:
                        return HttpResponseBadRequest(f"Related model with primary key {data[field.name]} does not exist.")
            
            instance = self.model(**data)
            instance.save()
            instance_dict = model_to_dict(instance)
            return Response(instance_dict, status=status.HTTP_201_CREATED)

    def serialize_instance(self, instance):

        instance_dict = model_to_dict(instance)
        return instance_dict

from .models import *  # Import your models

def generate_model_views():
    models = apps.get_models()
    views = []

    for model in models:
        class_name = f"{model.__name__}JSONView"
        view_class = type(class_name, (JSONDetailView,), {'model': model})
        views.append(view_class)

    return views

class PatientMedicationsView(APIView):
    def get(self, request, patient_id, *args, **kwargs):
        try:
            patient_receipts = Receipt.objects.filter(Patient_id=patient_id)
            medications = []

            for receipt in patient_receipts:
                receipt_medications = ReceiptMedication.objects.filter(Receipt=receipt)
                medications.extend(receipt_medication.DocMedPermission.Medication for receipt_medication in receipt_medications)

            medication_data = [model_to_dict(medication) for medication in medications]
            return Response(medication_data)

        except Exception as e:
            return HttpResponseBadRequest(f"Error: {str(e)}")
        

class DoctorMedicationsView(APIView):
    def get(self, request, doctor_id, *args, **kwargs):
        try:
            # Assuming doctor_id is the ID of the doctor
            doctor_permissions = DocMedPermission.objects.filter(Doctor_id=doctor_id)
            medications = [permission.Medication for permission in doctor_permissions]

            medication_data = [model_to_dict(medication) for medication in medications]
            return Response(medication_data)

        except Exception as e:
            return HttpResponseBadRequest(f"Error: {str(e)}")
        

class ReceiptMedicationByReceiptView(APIView):
    def get(self, request, receipt_id):
        try:
            doc_permission = ReceiptMedication.objects.filter(Receipt_id=receipt_id)
            doc_permission_ids = [getattr(instance, "DocMedPermission_id") for instance in doc_permission]
            print(doc_permission_ids)
            receipt_medications = DocMedPermission.objects.filter(id__in = doc_permission_ids)
            medication_ids = [getattr(instance, "Medication_id") for instance in receipt_medications]
            medication = Medication.objects.filter(id__in = medication_ids)
            data = [model_to_dict(item) for item in medication]

            return Response(data)
        except ReceiptMedication.DoesNotExist:
            return Response({"error": f"No ReceiptMedication found for Receipt with id {receipt_id}"}, status=404)
        
class MedicationSuggestion(APIView):
    def get(self, request, medicationstart):
        medicationstart_lower = medicationstart.lower()  # Convert query string to lowercase
        medications = Medication.objects.filter(MEDNAME__istartswith=medicationstart_lower)
        data = [model_to_dict(item)['MEDNAME'] for item in medications]
        return Response(data)
    

def update_used(request, receipt_id):
    # Retrieve the object to be updated
    receipt = get_object_or_404(Receipt, id=receipt_id)
    # Update the PERIOD field with the new value
    receipt.USED = 'Y'
    receipt.save()

    # Return a JSON response indicating success
    return JsonResponse({'status': 'success'})
