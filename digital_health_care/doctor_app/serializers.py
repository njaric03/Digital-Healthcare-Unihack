from rest_framework import serializers
from doctor_app.models import *

class SpecializationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialization
        fields = '__all__'

class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Doctor
        fields = '__all__'

class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = '__all__'

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medication
        fields = '__all__'

class MedForSpecSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedForSpec
        fields = '__all__'

class DocMedPermissionSerializer(serializers.ModelSerializer):
    class Meta:
        model = DocMedPermission
        fields = '__all__'

class ReceiptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receipt
        fields = '__all__'

class ReceiptMedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = ReceiptMedication
        fields = '__all__'

class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = '__all__'

class HasMedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = HasMedication
        fields = '__all__'