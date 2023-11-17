from django.contrib import admin
from .models import Specialization, Doctor, Patient, Medication, MedForSpec, DocMedPermission, Receipt, ReceiptMedication, Pharmacy, HasMedication

admin.site.register(Specialization)
admin.site.register(Doctor)
admin.site.register(Patient)
admin.site.register(Medication)
admin.site.register(MedForSpec)
admin.site.register(DocMedPermission)
admin.site.register(Receipt)
admin.site.register(ReceiptMedication)
admin.site.register(Pharmacy)
admin.site.register(HasMedication)