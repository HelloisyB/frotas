# Create your views here.

from django.shortcuts import render
from .models import Motorista

def listar_motoristas(request):
    motoristas_salvos = Motorista.objects.all()

    contexto = {
        'motoristas': motoristas_salvos
    }

    return render(request, 'motoristas/lista.html', contexto)
