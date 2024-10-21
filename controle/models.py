from django.db import models
from django.contrib.auth.models import User

class Conta(models.Model):
    TIPO_CONTA = [
        ('CC', 'Conta Corrente'),
        ('CP', 'Conta Poupança'),
    ]

    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    nome = models.CharField(max_length=100)
    tipo = models.CharField(max_length=2, choices=TIPO_CONTA)

    def __str__(self):
        return f"{self.nome} ({self.get_tipo_display()})"


class Transacao(models.Model):
    CATEGORIAS = [
        ('AL', 'Alimentação'),
        ('TR', 'Transporte'),
        ('SA', 'Saúde'),
        ('LA', 'Lazer'),
        ('SU', 'Supermercado'),
    ]
    TIPOS = [
        ('REC', 'RECEITA'),
        ('DSP', 'DESPESA'),
    ]
    conta = models.ForeignKey(Conta, on_delete=models.CASCADE)
    data = models.DateField()
    tipo = models.CharField(max_length=3, choices=TIPOS)  # 'RECEITA' ou 'DESPESA'
    categoria = models.CharField(max_length=2, choices=CATEGORIAS)
    valor = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
       return f"{self.get_tipo_display()}: {self.valor} em {self.data} ({self.get_categoria_display()})"
