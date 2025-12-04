from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    # -------------------------
    # Motoristas
    # -------------------------
    path('motoristas/', views.listar_motoristas, name='listar_motoristas'),
    path('motoristas/adicionar/', views.adicionar_motorista, name='adicionar_motorista'),
    path('motoristas/<int:pk>/', views.detalhe_motorista, name='detalhe_motorista'),
    path('motoristas/<int:pk>/editar/', views.alterar_motorista, name='alterar_motorista'),
    path('motoristas/<int:pk>/excluir/', views.excluir_motorista, name='excluir_motorista'),

    # histórico do motorista
    path('motoristas/<int:pk>/historico/', views.historico_motorista, name='historico_motorista'),

    # -------------------------
    # Veículos
    # -------------------------
    path('veiculos/', views.listar_veiculos, name='listar_veiculos'),
    path('veiculos/adicionar/', views.adicionar_veiculo, name='adicionar_veiculo'),
    path('veiculos/<int:pk>/editar/', views.alterar_veiculo, name='alterar_veiculo'),

    # histórico do veículo
    path('veiculos/<int:pk>/historico/', views.historico_veiculo, name='historico_veiculo'),

    # -------------------------
    # Viagens
    # -------------------------
    path('viagens/', views.listar_viagens, name='listar_viagens'),
    path('viagens/iniciar/', views.iniciar_viagem, name='iniciar_viagem'),
    path('viagens/<int:pk>/finalizar/', views.finalizar_viagem, name='finalizar_viagem'),

    # -------------------------
    # Manutenções
    # -------------------------
    path('manutencoes/', views.listar_manutencoes, name='listar_manutencoes'),
    path('manutencoes/solicitar/', views.solicitar_manutencao, name='solicitar_manutencao'),

    # NOVOS:
    path('manutencoes/<int:pk>/', views.detalhe_manutencao, name='detalhe_manutencao'),
    path('manutencoes/<int:pk>/concluir/', views.concluir_manutencao, name='concluir_manutencao'),
]
