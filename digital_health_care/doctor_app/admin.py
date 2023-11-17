from django.contrib import admin
from django.db import models
from .models import *




model_classes = [obj for name, obj in locals().items() if isinstance(obj, type) and issubclass(obj, models.Model)]

for model_class in model_classes:
    admin.site.register(model_class)
