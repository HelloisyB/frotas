from django.db import models

class Motorista(models.Model):
    nome = models.CharField(max_length=100)
    cnh = models.CharField(max_length=20, unique=True)
    categoria = models.CharField(max_length=5, default='')

    def __str__(self):
        return self.nome


class Veiculo(models.Model):
    placa = models.CharField(max_length=10, unique=True)
    modelo = models.CharField(max_length=100)
    ano = models.IntegerField()
    quilometragem = models.FloatField(default=0)

    def __str__(self):
        return f"{self.modelo} ({self.placa})"

class RegistroViagem(models.Model):
    motorista = models.ForeignKey(Motorista, on_delete=models.CASCADE)
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    data_saida = models.DateField()
    data_retorno = models.DateField(null=True, blank=True)
    km_saida = models.FloatField()
    km_retorno = models.FloatField(null=True, blank=True)

    def __str__(self):
        return f"Viagem de {self.motorista} - {self.veiculo}"


class SolicitacaoManutencao(models.Model):
    veiculo = models.ForeignKey(Veiculo, on_delete=models.CASCADE)
    data_solicitacao = models.DateField(auto_now_add=True, null=True)
    descricao_problema = models.TextField()
    status = models.CharField(
        max_length=20,
        choices=[
            ("Pendente", "Pendente"),
            ("Em andamento", "Em andamento"),
            ("Concluída", "Concluída"),
        ],
        default="Pendente"
    )

    def __str__(self):
        return f"Manutenção {self.id} - {self.veiculo.placa}"
