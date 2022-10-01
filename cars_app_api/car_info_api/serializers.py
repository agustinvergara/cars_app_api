from rest_framework import serializers
from .models import *
from .views import *

class CarsBrandsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brands
        fields = '__all__'

class CarsModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Model
        fields = '__all__'

class ModelVersionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Version
        fields = '__all__'

class ImagesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = '__all__'

class UnitModelSerializer(serializers.Serializer):
    model_id = serializers.IntegerField(read_only=False)
    brand_name = serializers.CharField(allow_blank=True, allow_null=True, max_length=70, required=False)
    segment_name = serializers.CharField(allow_blank=True, allow_null=True, max_length=70, required=False)
    model_name = serializers.CharField(allow_blank=True, allow_null=True, max_length=70, required=False)
    carrousel_images = ImagesSerializer(many=True)


class ModelVersionsSerializer(serializers.ModelSerializer):
    carrousel_images = ImagesSerializer(many=True)
    class Meta:
        model = Version
        filelds = ['__all__', 'carrousel_images']

class MdoelUnitVersionSerializer():
    pass