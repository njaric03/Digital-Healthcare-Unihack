# doctor_app/urls.py
from django.urls import path
from .views import DoctorViewSet

urlpatterns = [
    path('doctors/<int:pk>/', DoctorViewSet.as_view({'get': 'get'}), name='doctor-detail'),
]
