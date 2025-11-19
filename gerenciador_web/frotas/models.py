from django.db import models


#Gerenciamento
class Veiculo(models.Model):
    placa = models.CharField(max_length=20)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    km_atual = models.FloatField(default=0)

    def __str__(self):
        return f"{self.modelo} - {self.placa}"


class Motorista(models.Model):
    nome = models.CharField(max_length=200)
    cnh = models.CharField(max_length=50)
    telefone = models.CharField(max_length=20, blank=True, null=True)

    def __str__(self):
        return self.nome


class RegistroViagem(models.Model):
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    data_saida = models.DateTimeField(auto_now_add=True)
    km_saida = models.FloatField()
    data_retorno = models.DateTimeField(blank=True, null=True)
    km_retorno = models.FloatField(blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"{self.motorista} - {self.veiculo} ({self.data_saida.date()})"


class SolicitacaoManutencao(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    descricao_problema = models.TextField()
    data_solicitacao = models.DateTimeField(auto_now_add=True)
    atendida = models.BooleanField(default=False)

    def __str__(self):
        return f"Manutenção {self.veiculo} - {'Atendida' if self.atendida else 'Pendente'}"
