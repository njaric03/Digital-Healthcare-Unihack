from django.urls import path
from .views import generate_model_views

model_views = generate_model_views()


urlpatterns = []
for view_class in model_views:
    model_name = view_class.model.__name__.lower()
    urlpatterns.append(path(f'api/{model_name}/<int:pk>/', view_class.as_view(), name=f'{model_name}_json'))
    urlpatterns.append(path(f'api/{model_name}/', view_class.as_view(), name=f'{model_name}_all_json'))
    urlpatterns.append(path(f'api/{model_name}/post/', view_class.as_view(), name=f'{model_name}_post_json'))