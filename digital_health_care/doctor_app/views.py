from django.http import JsonResponse
from rest_framework import response
from django.views import View
from django.db.models import Model
from django.apps import apps
from django.urls import path
from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import Http404

from django.forms.models import model_to_dict
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

    def serialize_instance(self, instance):

        instance_dict = model_to_dict(instance)
        #instance_json = json.dumps(instance_dict)
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

model_views = generate_model_views()


urlpatterns = []
for view_class in model_views:
    model_name = view_class.model.__name__.lower()
    urlpatterns.append(path(f'api/{model_name}/<int:pk>/', view_class.as_view(), name=f'{model_name}_json'))
    urlpatterns.append(path(f'api/{model_name}/all/', view_class.as_view(), name=f'{model_name}_all_json'))
