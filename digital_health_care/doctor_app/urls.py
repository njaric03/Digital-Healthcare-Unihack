from django.urls import path
from .views import *

urlpatterns = [
    path('specializations/<int:pk>/', SpecializationViewSet.as_view(), name='specialization-detail'),
    path('specializations/', SpecializationViewSet.as_view(), name='specialization-list'),
    # Assuming you have a list view for specializations

    path('doctors/<int:pk>/', DoctorViewSet.as_view(), name='doctor-detail'),
    path('doctors/', DoctorViewSet.as_view(), name='doctor-list'),
    # Assuming you have a list view for doctors

    path('patients/<int:pk>/', PatientViewSet.as_view(), name='patient-detail'),
    path('patients/', PatientViewSet.as_view(), name='patient-list'),

    path('medications/<int:pk>/', MedicationViewSet.as_view(), name='medication-detail'),
    path('medications/', MedicationViewSet.as_view(), name='medication-list'),

    path('medforspecs/<int:pk>/', MedForSpecViewSet.as_view(), name='medforspec-detail'),
    path('medforspecs/', MedForSpecViewSet.as_view(), name='medforspec-list'),

    path('docmedpermissions/<int:pk>/', DocMedPermissionViewSet.as_view(), name='docmedpermission-detail'),
    path('docmedpermissions/', DocMedPermissionViewSet.as_view(), name='docmedpermission-list'),

    path('receipts/<int:pk>/', ReceiptViewSet.as_view(), name='receipt-detail'),
    path('receipts/', ReceiptViewSet.as_view(), name='receipt-list'),

    path('receiptmedications/<int:pk>/', ReceiptMedicationViewSet.as_view(), name='receiptmedication-detail'),
    path('receiptmedications/', ReceiptMedicationViewSet.as_view(), name='receiptmedication-list'),

    path('pharmacies/<int:pk>/', PharmacyViewSet.as_view(), name='pharmacy-detail'),
    path('pharmacies/', PharmacyViewSet.as_view(), name='pharmacy-list'),

    path('hasmedications/<int:pk>/', HasMedicationViewSet.as_view(), name='hasmedication-detail'),
    path('hasmedications/', HasMedicationViewSet.as_view(), name='hasmedication-list'),
]
