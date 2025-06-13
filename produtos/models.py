from django.db import models
from django.utils import timezone

class Produto(models.Model):
    COR_CHOICES = [
        ('Azul', 'Azul'),
        ('Vermelho', 'Vermelho'),
        ('Verde', 'Verde'),
        ('Amarelo', 'Amarelo'),
        ('Branco', 'Branco'),
        ('Preto', 'Preto'),
        ('Marrom', 'Marrom'),
    ]

    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=70)
    preco_compra = models.FloatField()
    preco_venda = models.FloatField()
    data_fabricacao = models.DateField(default=timezone.now())
    imagem = models.CharField(max_length=25)

    def __str__(self):
        return f'{self.nome} (Código: {self.codigo})'