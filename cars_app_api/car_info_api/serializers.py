from dataclasses import field
from pyexpat import model
from rest_framework import serializers
from .models import *
from .views import *

class CarsBrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = '__all__'

class CarsModelSerializer(serializers.ModelSerializer):
    # brand_name = CarsBrandsSerializer(read_only=True)
    class Meta:
        model = Model
        fields = '__all__'

class UnitModelSerializer(serializers.Serializer):
    model_id = serializers.IntegerField(read_only=False)
    brand_name = serializers.CharField(allow_blank=True, allow_null=True, max_length=70, required=False)
    segment_name = serializers.CharField(allow_blank=True, allow_null=True, max_length=70, required=False)
    model_name = serializers.CharField(allow_blank=True, allow_null=True, max_length=70, required=False)
    model_image_1 = serializers.CharField(allow_blank=True, allow_null=True, max_length=700, required=False)
    model_image_2 = serializers.CharField(allow_blank=True, allow_null=True, max_length=700, required=False)
    model_image_3 = serializers.CharField(allow_blank=True, allow_null=True, max_length=700, required=False)

class ModelVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = '__all__'