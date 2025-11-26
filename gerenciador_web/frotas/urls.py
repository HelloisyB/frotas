#urlpatterns = [
    
#python manage.py makemigrations]

from django.urls import include, path

from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('motoristas/', views.listar_motoristas, name='listar_motoristas'),
    path('veiculos/', views.listar_veiculos, name='listar_veiculos'),
    path('manutencoes/', views.listar_manutencoes, name='listar_manutencoes'),
    path('viagens/', views.listar_viagens, name='listar_viagens'),
]
