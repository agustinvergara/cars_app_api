from django.urls import path
from . import views

app_name = 'car_info_api'

urlpatterns = [
    #endpoint to send a json with all the brands
    path('brands/', views.cars_brand_serializer, name='all_brands_serializer'),
    #endpoint to send a json with all models on one brand
    path('brand/<str:brand_name>/models/', views.cars_models_serializer, name='all_models_serializer'),
    path('brand/model/<str:model_name>', views.car_model_unit_serializer, name='model_unit_serializer'),
    path('brand/<str:model_name>/versions', views.model_version_serializer, name='model_version_serializer'),
]
