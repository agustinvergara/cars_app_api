from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import *

class CarsBrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = '__all__'

class CarsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__' #['model_id', 'brand_id', 'segment_id', 'model_name']
