from django.shortcuts import render
from rest_framework import viewsets
from doctor_app.models import *
from doctor_app.serializers import *
from django.http import HttpResponse

# Create your views here.
class SpecializationViewSet(viewsets.ModelViewSet):
    queryset = Specialization.objects.all()
    serializer_class = SpecializationSerializer


class DoctorViewSet(viewsets.ModelViewSet):
    queryset = Doctor.objects.all()
    serializer_class = DoctorSerializer

class PatientViewSet(viewsets.ModelViewSet):
    queryset = Patient.objects.all()
    serializer_class = PatientSerializer

class MedicationViewSet(viewsets.ModelViewSet):
    queryset = Medication.objects.all()
    serializer_class = MedicationSerializer

class MedForSpecViewSet(viewsets.ModelViewSet):
    queryset = MedForSpec.objects.all()
    serializer_class = MedForSpecSerializer

class DocMedPermissionViewSet(viewsets.ModelViewSet):
    queryset = DocMedPermission.objects.all()
    serializer_class = DocMedPermissionSerializer

class ReceiptViewSet(viewsets.ModelViewSet):
    queryset = Receipt.objects.all()
    serializer_class = ReceiptSerializer

class ReceiptMedicationViewSet(viewsets.ModelViewSet):
    queryset = ReceiptMedication.objects.all()
    serializer_class = ReceiptMedicationSerializer

class PharmacyViewSet(viewsets.ModelViewSet):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer

class HasMedicationViewSet(viewsets.ModelViewSet):
    queryset = HasMedication.objects.all()
    serializer_class = HasMedicationSerializer