#urlpatterns = [
    
#python manage.py makemigrations]

from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_veiculos, name='listar_veiculos'),
    path('motoristas/', views.listar_motoristas, name='listar_motoristas'),
    path('viagens/', views.listar_viagens, name='listar_viagens'),
    path('manutencoes/', views.listar_manutencoes, name='listar_manutencoes'),
]
