from django.urls import path
from . import views

app_name = 'car_info_api'

urlpatterns = [
    #endpoint to send a json with all the brands
    path('brands/', views.cars_brand_serializer, name='all_brands_serializer'),
    #endpoint to send a json with all models on one brand
    path('brand/<int:brand_id>/models/', views.cars_models_serializer, name='all_models_serializer'),
]
