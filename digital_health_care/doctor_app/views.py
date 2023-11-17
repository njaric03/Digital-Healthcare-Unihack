from django.shortcuts import render
from doctor_app.models import *
from doctor_app.serializers import *
from django.http import HttpResponse
from django.forms.models import model_to_dict
import json

# Create your views here.
class SpecializationViewSet(viewsets.ModelViewSet):
    
    queryset = Specialization.objects.all()

    def get(self, request, pk = None):
        try:
            instance = self.queryset.get(pk = pk)
            instance_dict = model_to_dict(instance)
            instance_json = json.dumps(instance_dict)
            return HttpResponse(instance_json, content_type = 'application/json')
        except Doctor.DoesNotExist:
            return HttpResponse({"error": "Doctor not found"}, status=404)

