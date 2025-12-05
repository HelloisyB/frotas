from django.test import TestCase
from frotas.models import Motorista, Veiculo, RegistroViagem

class RegistroViagemModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.motorista = Motorista.objects.create(nome='Test Motorista', cnh='ABC1234')
        cls.veiculo = Veiculo.objects.create(modelo='Fusca', placa='ABC-1234', ano=1990)

    def test_criacao_viagem_com_valores_padrao(self):
        viagem = RegistroViagem.objects.create(
            motorista=self.motorista,
            veiculo=self.veiculo,
            km_saida=100
        )
        self.assertIsNone(viagem.km_retorno)  # por padrão deve ser None
        self.assertIsNotNone(viagem.data_saida)  # deve ter preenchido a data de saída

    def test_viagem_requer_motorista_e_veiculo(self):
        viagem = RegistroViagem.objects.create(
            motorista=self.motorista,
            veiculo=self.veiculo,
            km_saida=50
        )
        self.assertEqual(viagem.motorista.nome, 'Test Motorista')
        self.assertEqual(viagem.veiculo.modelo, 'Fusca')
