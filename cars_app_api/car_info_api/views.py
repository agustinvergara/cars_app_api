import imp
from symbol import return_stmt
from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import *
from .urls import *
from .serializers import *

@api_view(['GET', 'POST'])
def cars_brand_serializer(request):
    try:
        cars_brands = Brands.objects.all()
    except Brands.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET' or 'POST':
        cars_brands_serialized = CarsBrandsSerializer(cars_brands, many=True) #many=True to serialize all queryset objects
        return Response(cars_brands_serialized.data)

@api_view(['GET', 'POST'])
def cars_models_serializer(request, brand_id):
    try:
        brand_models = Model.objects.filter(pk=brand_id)
    except Model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET' or 'POST':
        cars_models_serialized = CarsModelSerializer(brand_models, many=True)
        return Response(cars_models_serialized.data)
 
@api_view(['GET','POST'])
def car_model_unit_serializer(request, model_id):
    car_model_queryset = Model.objects.select_related('brand').get(pk=model_id)
    car_model_segment = Segment.objects.get(pk=car_model_queryset.segment)
    model_unit_data = {
        'model_id':car_model_queryset.model_id,
        'brand_name':car_model_queryset.brand.brand_name,
        'segment_name':car_model_segment.segment_name,
        'model_name':car_model_queryset.model_name,
        'model_image_1':car_model_queryset.model_image_1,
        'model_image_2':car_model_queryset.model_image_2,
        'model_image_3':car_model_queryset.model_image_3
    }

    if request.method == 'GET' or 'POST':
        unit_model_serializer = UnitModelSerializer(data=model_unit_data)
        unit_model_serializer.is_valid()
        return Response(unit_model_serializer.data)