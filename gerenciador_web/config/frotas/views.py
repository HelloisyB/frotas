from django.shortcuts import render
from .models import Veiculo, Motorista, RegistroViagem, SolicitacaoManutencao

def listar_veiculos(request):
    veiculos = Veiculo.objects.all()
    contexto = {'veiculos': veiculos}
    return render(request, 'frota/lista_veiculos.html', contexto)


def listar_motoristas(request):
    motoristas = Motorista.objects.all()
    contexto = {'motoristas': motoristas}
    return render(request, 'frota/lista_motoristas.html', contexto)


def listar_viagens(request):
    viagens = RegistroViagem.objects.all()
    contexto = {'viagens': viagens}
    return render(request, 'frota/lista_viagens.html', contexto)


def listar_manutencoes(request):
    manutencoes = SolicitacaoManutencao.objects.all()
    contexto = {'manutencoes': manutencoes}
    return render(request, 'frota/lista_manutencoes.html', contexto)
