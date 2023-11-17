from django.apps import apps
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.http import Http404
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
