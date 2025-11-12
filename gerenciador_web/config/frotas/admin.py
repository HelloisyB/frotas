from django.contrib import admin
from .models import Motorista, Veiculo, RegistroViagem, SolicitacaoManutencao

# Registrar os modelos no painel admin
admin.site.register(Motorista)
admin.site.register(Veiculo)
admin.site.register(RegistroViagem)
admin.site.register(SolicitacaoManutencao)
