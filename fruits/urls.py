from django.urls import path
from rest_framework.generics import ListCreateAPIView, UpdateAPIView

from .models import Fruit
from .serializer import FruitSerializer
from .views import index, detail_fruit, delete_fruit, create_fruit, update_fuit, liste_fruit, ListeFruitApi, \
    FruitViewSet

app_name = 'fruits_app'


urlpatterns = [
    path('', index, name='home_page'),
    path('fruit/creation', create_fruit, name='create_fruit'),
    path('fruit/modification/<int:pk>', update_fuit, name='modification_fruit'),
    path('fruit/detail/<int:pk>', detail_fruit, name='detail_fruit'),
    path('fruit/suppresion/<int:pk>', delete_fruit, name='supprimer_fruit'),
    path('fruit/liste', liste_fruit, name='list_fruit'),

    # api
    path('api/fruit/liste', ListCreateAPIView.as_view(queryset=Fruit.objects.all(), serializer_class=FruitSerializer), name='ListeFruitApi'),
    path('api/fruit/update/<int:pk>', UpdateAPIView.as_view(queryset=Fruit.objects.all(), serializer_class=FruitSerializer), name='Update'),
    path('api/viewset',  FruitViewSet.as_view({'get': 'list', 'post': 'update'}, name='Viewset configuration')),

]