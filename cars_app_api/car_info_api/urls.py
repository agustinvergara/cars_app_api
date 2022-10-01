from django.urls import path
from . import views

app_name = 'car_info_api'

urlpatterns = [
    #endpoint to send a json with all the brands
    path('brands/', views.all_cars_brand, name='all_brands_serializer'),
    #endpoint to send a json with all models on one brand
    path('brand/<str:brand_name>/models/', views.all_brand_models, name='all_models_serializer'),
    #endpoint to send one model for a given model_name (for the catalog brand index)
    path('brand/model/<str:model>', views.car_model_unit_serializer, name='model_unit_serializer'),
    path('brand/<str:model>/versions', views.model_version_serializer, name='model_version_serializer'),
]
