from django.db import models

class Motorista(models.Model):
    nome = models.CharField(max_length=100)
    cnh = models.CharField(max_length=20)

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    modelo = models.CharField(max_length=100)
    placa = models.CharField(max_length=10)
    ano = models.IntegerField()
    km_atual = models.FloatField(default=0)
    disponivel = models.BooleanField(default=True)

    def __str__(self):
        return f"{self.modelo} - {self.placa}"


class RegistroViagem(models.Model):
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    km_saida = models.FloatField()
    km_retorno = models.FloatField(null=True, blank=True)
    data_saida = models.DateTimeField(auto_now_add=True)
    data_retorno = models.DateTimeField(null=True, blank=True)
    observacoes = models.TextField(blank=True)

    def __str__(self):
        return f"Viagem de {self.motorista} com {self.veiculo}"


class SolicitacaoManutencao(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    descricao_problema = models.TextField()
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    concluida = models.BooleanField(default=False)

    def __str__(self):
        return f"Manutenção - {self.veiculo.placa}"

