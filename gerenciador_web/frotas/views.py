from django.shortcuts import render, get_object_or_404, redirect
from .models import Motorista, SolicitacaoManutencao, Veiculo

def dashboard(request):
    return render(request, 'frotas/dashboard.html')

def listar_motoristas(request):
    motoristas = Motorista.objects.all()
    return render(request, 'motoristas/lista_motoristas.html', {'motoristas': motoristas})

def adicionar_motorista(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        cnh = request.POST.get('cnh')
        Motorista.objects.create(nome=nome, cnh=cnh)
        return redirect('listar_motoristas')
    return render(request, 'motoristas/form_motorista.html')

def alterar_motorista(request, pk):
    motorista = get_object_or_404(Motorista, pk=pk)
    if request.method == 'POST':
        motorista.nome = request.POST.get('nome')
        motorista.cnh = request.POST.get('cnh')
        motorista.save()
        return redirect('detalhe_motorista', pk=motorista.id)
    return render(request, 'motoristas/form_motorista.html', {'motorista': motorista})

def detalhe_motorista(request, pk):
    motorista = get_object_or_404(Motorista, pk=pk)
    return render(request, 'motoristas/detalhe_motorista.html', {'motorista': motorista})

def excluir_motorista(request, pk):
    motorista = get_object_or_404(Motorista, pk=pk)
    if request.method == 'POST':
        motorista.delete()
        return redirect('listar_motoristas')
    return render(request, 'motoristas/confirmar_exclusao_motorista.html', {'motorista': motorista})


def listar_veiculos(request):
    if request.method == 'POST':
        modelo = request.POST.get('modelo')
        placa = request.POST.get('placa')
        if modelo and placa:
            Veiculo.objects.create(modelo=modelo, placa=placa)
            return redirect('listar_veiculos')

    veiculos = Veiculo.objects.all().order_by('id')
    return render(request, 'veiculos.html', {'veiculos': veiculos})


def listar_manutencoes(request):
    manutencoes = SolicitacaoManutencao.objects.all()
    return render(request, 'manutencoes.html', {'manutencoes': manutencoes})

def listar_viagens(request):
    return render(request, 'viagens/lista_viagens.html')
