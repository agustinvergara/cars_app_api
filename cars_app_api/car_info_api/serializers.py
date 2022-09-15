from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import *

class CarsBrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = ['brand_id', 'brand_name']

class CarsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        field = '__all__'