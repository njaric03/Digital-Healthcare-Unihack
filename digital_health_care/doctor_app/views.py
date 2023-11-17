from django.shortcuts import render
from doctor_app.models import *
from doctor_app.serializers import *
from django.http import HttpResponse
from django.forms.models import model_to_dict
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json

# Create your views here.
class SpecializationViewSet(APIView):
    
    queryset = Specialization.objects.all()

    def get(self, request, pk = None):
        try:
            instance = self.queryset.get(pk = pk)
            instance_dict = model_to_dict(instance)
            instance_json = json.dumps(instance_dict)
            return Response(instance_dict)
        except Doctor.DoesNotExist:
                return Response({"error": "Specialization not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request, pk = None):
        try:
            instance = self.queryset.get(pk = pk)
            instance_dict = model_to_dict(instance)
            return Response(instance_dict)
        except Doctor.DoesNotExist:
                return Response({"error": "Specialization not found"}, status=status.HTTP_404_NOT_FOUND)


class DoctorViewSet(APIView):

    queryset = Doctor.objects.all()

    def get(self, request, pk = None):
        try:
            instance = self.queryset.get(pk = pk)
            instance_dict = model_to_dict(instance)
            instance_json = json.dumps(instance_dict)
            return Response(instance_dict)
        except Doctor.DoesNotExist:
            return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request, pk = None):
        try:
            instance = self.queryset.get(pk = pk)
            instance_dict = model_to_dict(instance)
            instance_json = json.dumps(instance_dict)
            return Response(instance_dict)
        except Doctor.DoesNotExist:
            return Response({"error": "Doctor not found"}, status=status.HTTP_404_NOT_FOUND)
        
class PatientViewSet(APIView):

    queryset = Patient.objects.all()

    def get(self, request, pk = None):
        try:
            instance = self.queryset.get(pk = pk)
            instance_dict = model_to_dict(instance)
            instance_json = json.dumps(instance_dict)
            return Response(instance_dict)
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)

    def post(self, request, pk = None):
        try:
            instance = self.queryset.get(pk = pk)
            instance_dict = model_to_dict(instance)
            instance_json = json.dumps(instance_dict)
            return Response(instance_dict)
        except Patient.DoesNotExist:
            return Response({"error": "Patient not found"}, status=status.HTTP_404_NOT_FOUND)
        
class MedicationViewSet(APIView):

    queryset = Medication.objects.all()

    def get(self, request, pk = None):
        try:
            instance = self.queryset.get(pk = pk)
            instance_dict = model_to_dict(instance)
            instance_json = json.dumps(instance_dict)
            return Response(instance_dict)
        except Medication.DoesNotExist:
            return Response({"error": "Medication not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request, pk = None):
        try:
            instance = self.queryset.get(pk = pk)
            instance_dict = model_to_dict(instance)
            instance_json = json.dumps(instance_dict)
            return Response(instance_dict)
        except Medication.DoesNotExist:
            return Response({"error": "Medication not found"}, status=status.HTTP_404_NOT_FOUND)
        
class MedForSpecViewSet(APIView):
    
    queryset = MedForSpec.objects.all()

    def get(self, request, pk = None):
        try:
            instance = self.queryset.get(pk = pk)
            instance_dict = model_to_dict(instance)
            instance_json = json.dumps(instance_dict)
            return Response(instance_dict)

        except MedForSpec.DoesNotExist:
            return Response({"error": "MedForSpec not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request, pk = None):
        try:
            instance = self.queryset.get(pk = pk)
            instance_dict = model_to_dict(instance)
            instance_json = json.dumps(instance_dict)

            return Response(instance_dict)
        except MedForSpec.DoesNotExist:
            return Response({"error": "MedForSpec not found"}, status=status.HTTP_404_NOT_FOUND)
        
class DocMedPermissionViewSet(APIView):

    queryset = DocMedPermission.objects.all()

    def get(self, request, pk = None):
        try:
            instance = self.queryset.get(pk = pk)
            instance_dict = model_to_dict(instance)
            instance_json = json.dumps(instance_dict)

            return Response(instance_dict)
        except DocMedPermission.DoesNotExist:
            return Response({"error": "DocMedPermission not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request, pk = None):
        try:
            instance = self.queryset.get(pk = pk)
            instance_dict = model_to_dict(instance)

            instance_json = json.dumps(instance_dict)
            return Response(instance_dict)
        except DocMedPermission.DoesNotExist:
            return Response({"error": "DocMedPermission not found"}, status=status.HTTP_404_NOT_FOUND)
        
class ReceiptViewSet(APIView):

    queryset = Receipt.objects.all()

    def get(self, request, pk = None):
        try:
            instance = self.queryset.get(pk = pk)
            instance_dict = model_to_dict(instance)

            instance_json = json.dumps(instance_dict)
            return Response(instance_dict)
        except Receipt.DoesNotExist:
            return Response({"error": "Receipt not found"}, status=status.HTTP_404_NOT_FOUND)
        
    def post(self, request, pk = None):
        try:
            instance = self.queryset.get(pk = pk)
            instance_dict = model_to_dict(instance)

            instance_json = json.dumps(instance_dict)
            return Response(instance_dict)
        except Receipt.DoesNotExist:
            return Response({"error": "Receipt not found"}, status=status.HTTP_404_NOT_FOUND)
        
class ReceiptMedicationViewSet(APIView):

    queryset = ReceiptMedication.objects.all()

    def get(self, request, pk = None):
        try:
            instance = self.queryset.get(pk = pk)
            instance_dict = model_to_dict(instance)

            instance_json = json.dumps(instance_dict)
            return Response(instance_dict)
        except ReceiptMedication.DoesNotExist:
            return Response({"error": "ReceiptMedication not found"}, status=status.HTTP_404_NOT_FOUND)
    
    def post(self, request, pk = None):
        try:
            instance = self.queryset.get(pk = pk)
            instance_dict = model_to_dict(instance)

            instance_json = json.dumps(instance_dict)
            return Response(instance_dict)
        except ReceiptMedication.DoesNotExist:
            return Response({"error": "ReceiptMedication not found"}, status=status.HTTP_404_NOT_FOUND)

class PharmacyViewSet(APIView):
    
        queryset = Pharmacy.objects.all()
    
        def get(self, request, pk = None):
            try:
                instance = self.queryset.get(pk = pk)
                instance_dict = model_to_dict(instance)
    
                instance_json = json.dumps(instance_dict)
                return Response(instance_dict)
            except Pharmacy.DoesNotExist:
                return Response({"error": "Pharmacy not found"}, status=status.HTTP_404_NOT_FOUND)
            
        def post(self, request, pk = None):
            try:
                instance = self.queryset.get(pk = pk)
                instance_dict = model_to_dict(instance)
    
                instance_json = json.dumps(instance_dict)
                return Response(instance_dict)
            except Pharmacy.DoesNotExist:
                return Response({"error": "Pharmacy not found"}, status=status.HTTP_404_NOT_FOUND)

class HasMedicationViewSet(APIView):
    
        queryset = HasMedication.objects.all()
    
        def get(self, request, pk = None):
            try:
                instance = self.queryset.get(pk = pk)
                instance_dict = model_to_dict(instance)
    
                instance_json = json.dumps(instance_dict)
                return Response(instance_dict)
            except HasMedication.DoesNotExist:
                return Response({"error": "HasMedication not found"}, status=status.HTTP_404_NOT_FOUND)
            
        def post(self, request, pk = None):
            try:
                instance = self.queryset.get(pk = pk)
                instance_dict = model_to_dict(instance)
    
                instance_json = json.dumps(instance_dict)
                return Response(instance_dict)
            except HasMedication.DoesNotExist:
                return Response({"error": "HasMedication not found"}, status=status.HTTP_404_NOT_FOUND)