from django.contrib import admin
from .models import Veiculo, Motorista, RegistroViagem, SolicitacaoManutencao

# Register your models here.
admin.site.register(Veiculo)
admin.site.register(Motorista)
admin.site.register(RegistroViagem)
admin.site.register(SolicitacaoManutencao)
