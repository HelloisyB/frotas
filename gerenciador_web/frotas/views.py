from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import Motorista, Veiculo, RegistroViagem, SolicitacaoManutencao

# -------------------------
# Dashboard
# -------------------------
def dashboard(request):
    return render(request, 'frotas/dashboard.html')


# -------------------------
# Motoristas
# -------------------------
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


# -------------------------
# Veículos
# -------------------------
def listar_veiculos(request):
    veiculos = Veiculo.objects.all().order_by('id')
    return render(request, 'frotas/veiculos.html', {'veiculos': veiculos})

def adicionar_veiculo(request):
    if request.method == 'POST':
        modelo = request.POST.get('modelo')
        placa = request.POST.get('placa')
        ano = request.POST.get('ano')
        km_atual = request.POST.get('km_atual') or 0

        Veiculo.objects.create(
            modelo=modelo,
            placa=placa,
            ano=ano,
            km_atual=km_atual
        )
        return redirect('listar_veiculos')

    return render(request, 'frotas/form_veiculo.html', {'titulo': 'Adicionar Veículo'})

def alterar_veiculo(request, pk):
    veiculo = get_object_or_404(Veiculo, pk=pk)
    if request.method == 'POST':
        veiculo.modelo = request.POST.get('modelo')
        veiculo.placa = request.POST.get('placa')
        veiculo.ano = request.POST.get('ano')
        veiculo.km_atual = request.POST.get('km_atual')
        veiculo.save()
        return redirect('listar_veiculos')

    return render(request, 'frotas/form_veiculo.html', {'veiculo': veiculo, 'titulo': 'Editar Veículo'})


# -------------------------
# Viagens
# -------------------------
def listar_viagens(request):
    viagens = RegistroViagem.objects.all().order_by('-data_saida')
    return render(request, 'viagens/lista_viagens.html', {'viagens': viagens})

def iniciar_viagem(request):
    motoristas = Motorista.objects.all()
    veiculos = Veiculo.objects.all()
    
    if request.method == 'POST':
        motorista_id = request.POST.get('motorista')
        veiculo_id = request.POST.get('veiculo')
        km_saida = request.POST.get('km_saida')
        observacoes = request.POST.get('observacoes', '')

        motorista = get_object_or_404(Motorista, pk=motorista_id)
        veiculo = get_object_or_404(Veiculo, pk=veiculo_id)

        RegistroViagem.objects.create(
            motorista=motorista,
            veiculo=veiculo,
            km_saida=km_saida,
            observacoes=observacoes
        )

        return redirect('listar_viagens')

    return render(request, 'viagens/form_viagem.html', {'motoristas': motoristas, 'veiculos': veiculos})

def finalizar_viagem(request, pk):
    viagem = get_object_or_404(RegistroViagem, pk=pk)

    if request.method == 'POST':
        viagem.km_retorno = request.POST.get('km_retorno')
        viagem.data_retorno = timezone.now()
        viagem.observacoes = request.POST.get('observacoes', viagem.observacoes)
        viagem.save()

        viagem.veiculo.km_atual = viagem.km_retorno
        viagem.veiculo.save()

        return redirect('listar_viagens')

    return render(request, 'viagens/finalizar_viagem.html', {'viagem': viagem})


def listar_manutencoes(request):
    manutencoes = SolicitacaoManutencao.objects.all()
    return render(request, 'manutencoes/listar_manutencoes.html', {'manutencoes': manutencoes})

def solicitar_manutencao(request):
    veiculos = Veiculo.objects.all()

    if request.method == 'POST':
        veiculo_id = request.POST.get('veiculo')
        descricao = request.POST.get('descricao_problema', '')

        veiculo = get_object_or_404(Veiculo, pk=veiculo_id)

        SolicitacaoManutencao.objects.create(
            veiculo=veiculo,
            descricao_problema=descricao
        )

        return redirect('listar_manutencoes')

    return render(request, 'manutencoes/form_manutencao.html', {'veiculos': veiculos})
