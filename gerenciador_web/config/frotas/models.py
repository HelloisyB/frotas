
# Create your models here.
from django.db import models

class Veiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    quilometragem = models.FloatField(default=0)

    def __str__(self):
        return f"{self.modelo} ({self.placa})"


class Motorista(models.Model):
    nome = models.CharField(max_length=100)
    cnh = models.CharField(max_length=20, unique=True)
    categoria = models.CharField(max_length=5)

    def __str__(self):
        return self.nome


class RegistroViagem(models.Model):
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    data_saida = models.DateTimeField(auto_now_add=True)
    km_saida = models.FloatField()
    data_retorno = models.DateTimeField(blank=True, null=True)
    km_retorno = models.FloatField(blank=True, null=True)

    def __str__(self):
        return f"Viagem de {self.motorista.nome} com {self.veiculo.placa}"

class SolicitacaoManutencao(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    descricao_problema = models.TextField()
    status = models.CharField(max_length=20, default='Pendente')

    def __str__(self):
        return f"{self.veiculo.placa} - {self.status}"
