from django.urls import path
from .views import index, detail_fruit, delete_fruit, create_fruit, update_fuit, liste_fruit


app_name = 'fruits_app'


urlpatterns = [
    path('', index, name='home_page'),
    path('fruit/creation', create_fruit, name='create_fruit'),
    path('fruit/modification/<int:pk>', update_fuit, name='modification_fruit'),
    path('fruit/detail/<int:pk>', detail_fruit, name='detail_fruit'),
    path('fruit/suppresion/<int:pk>', delete_fruit, name='supprimer_fruit'),
    path('fruit/liste', liste_fruit, name='list_fruit'),
]