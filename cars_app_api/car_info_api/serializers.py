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

# class CarsModelSerializer(serializers.Serializer):
#     model_id = serializers.IntegerField(read_only=True)
#     model_name = serializers.CharField(allow_blank=True, allow_null=True, max_length=70, required=False)
#     model_image = serializers.CharField(allow_blank=True, allow_null=True, max_length=700, required=False)
#     brand = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=Brands.objects.all(), required=False)
#     segment = serializers.PrimaryKeyRelatedField(allow_null=True, queryset=Segment.objects.all(), required=False)