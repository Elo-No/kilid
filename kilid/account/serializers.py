
from rest_framework import serializers
from .models import CustomUser
import json
from django.conf import settings
from django.contrib.sites.models import Site

class CustomUserSerializers(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['my_file', 'size','my_name']
        # fields = '__all__'
