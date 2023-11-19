from django.urls import path
from .views import generate_model_views, update_used
from .views import *
from django.contrib.auth import authenticate
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse



app_name = 'doctor_app'

model_views = generate_model_views()


urlpatterns = []
for view_class in model_views:
    model_name = view_class.model.__name__.lower()
    urlpatterns.append(path(f'api/{model_name}/<int:pk>/', view_class.as_view(), name=f'{model_name}_json'))
    urlpatterns.append(path(f'api/{model_name}/', view_class.as_view(), name=f'{model_name}_all_json'))
    urlpatterns.append(path(f'api/{model_name}/post/', view_class.as_view(), name=f'{model_name}_post_json'))

urlpatterns += [
        path('api/patient/<int:patient_id>/medications/', PatientMedicationsView.as_view(), name='patient_medications'),
        path('api/receipt/<int:receipt_id>/medications/', ReceiptMedicationByReceiptView.as_view(), name='receipt_medications'),
        path('api/medicationsuggestion/<str:medicationstart>/', MedicationSuggestion.as_view(), name='medication-suggestion'),
        path('api/receipt/update_used/<int:receipt_id>/', update_used, name='update_used')
,
        path('api/csrf-token/', CsrfToken.as_view(), name='csrf-token'),
        path('api/login/', LoginView.as_view(), name='login'),
        path('api/register/', RegisterView.as_view(), name='register'),
        path('api/token/renew', TokenRenewalView.as_view(), name='token-renew'),
]