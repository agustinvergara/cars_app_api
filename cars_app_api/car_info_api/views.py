import imp
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
        car_brand = Brands.objects.get(pk=brand_id)
        brand_models = Model.objects.filter(brand_id=1)
    except Model.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET' or 'POST':
        cars_models_serialized = CarsModelSerializer(brand_models, many=True)
        return Response(cars_models_serialized.data)