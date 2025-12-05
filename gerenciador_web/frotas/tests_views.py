from django.test import TestCase
from django.urls import reverse

from frotas.models import Veiculo, Motorista, RegistroViagem, SolicitacaoManutencao


class FrotasViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Criando Motorista e Veículo
        cls.motorista1 = Motorista.objects.create(nome='João Silva', cnh='123456789')
        cls.veiculo1 = Veiculo.objects.create(modelo='Fiat Uno', placa='ABC-1234')
        
        # Criando Registro de Viagem
        cls.registro1 = RegistroViagem.objects.create(
            motorista=cls.motorista1, 
            veiculo=cls.veiculo1, 
            km_saida=1000
        )
        
        # Criando Solicitação de Manutenção
        cls.solicitacao1 = SolicitacaoManutencao.objects.create(
            veiculo=cls.veiculo1, 
            descricao='Troca de óleo'
        )

    def test_adicionar_registro_viagem(self):
        url = reverse('adicionar_registro_viagem')
        dados = {
            'motorista': self.motorista1.id,
            'veiculo': self.veiculo1.id,
            'km_saida': 1500
        }
        self.client.post(url, data=dados)
        self.assertTrue(RegistroViagem.objects.filter(km_saida=1500).exists())

    def test_adicionar_solicitacao_manutencao(self):
        url = reverse('adicionar_solicitacao_manutencao')
        dados = {
            'veiculo': self.veiculo1.id,
            'descricao': 'Troca de pneus'
        }
        self.client.post(url, data=dados)
        self.assertTrue(SolicitacaoManutencao.objects.filter(descricao='Troca de pneus').exists())
