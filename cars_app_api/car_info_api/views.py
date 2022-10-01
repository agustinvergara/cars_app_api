from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .serializers import *

#API ENDPOINT THAT THROWS ALL BRANDS DATA
@api_view(['GET', 'POST'])
def all_cars_brand(request):
    try:
        cars_brands = Brands.objects.all()
    except Brands.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET' or 'POST':
        cars_brands_serialized = CarsBrandsSerializer(cars_brands, many=True) #many=True to serialize all queryset objects
        return Response(cars_brands_serialized.data)

#API ENDPOINT THAT THROWS MODELS DATA FROM A GIVEN BRAND
@api_view(['GET', 'POST'])
def all_brand_models(request, brand_name):
    try:
        brand = Brands.objects.get(brand_name=brand_name)
        brand_models = Model.objects.filter(brand=brand.brand_id)
    except Model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET' or 'POST':
        cars_models_serialized = CarsModelSerializer(brand_models, many=True)
        return Response(cars_models_serialized.data)
 
 #API ENDPOINT FOR GIVEN MODEL DATA 
@api_view(['GET','POST'])
def car_model_unit_serializer(request, model):
    try:
        car_model_queryset = Model.objects.select_related('brand', 'segment').get(model_name=model)
        model_images_queryset = Image.objects.filter(modelimage__model=car_model_queryset.model_id)
        model_unit_data = {
            'model_id':car_model_queryset.model_id,
            'brand_name':car_model_queryset.brand.brand_name,
            'segment_name':car_model_queryset.segment.segment_name,
            'model_name':car_model_queryset.model_name,
            'carrousel_images': model_images_queryset
        }
    except Model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET' or 'POST':
        unit_model_serializer = UnitModelSerializer(model_unit_data)
        # unit_model_serializer.is_valid()
        return Response(unit_model_serializer.data)

#API ENDPOINT FOR VERSIONS OF A GIVEN MODEL
@api_view(['GET','POST'])
def model_version_serializer(request, model):
    try:
        model = Model.objects.get(model_name=model_name)
        versions = Version.objects.filter(model=model.model_id)
    except Version.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET' or 'POST':
        versions_serializer = ModelVersionSerializer(versions, many=True)
        return Response(versions_serializer.data)

