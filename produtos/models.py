from django.db import models
from django.utils import timezone

class Produto(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=70)
    preco_compra = models.DecimalField(max_digits=8, decimal_places=2)
    preco_venda = models.DecimalField(max_digits=8, decimal_places=2)
    descricao = models.CharField(max_length=255, default='Sem descrição')
    data_fabricacao = models.DateField(default=timezone.now())
    cor = models.CharField(max_length=20, choices=[
        ('Azul', 'Azul'),
        ('Vermelho', 'Vermelho'),
        ('Verde', 'Verde'),
        ('Amarelo', 'Amarelo'),
        ('Branco', 'Branco'),
        ('Preto', 'Preto'),
        ('Marrom', 'Marrom'),
    ])
    imagem = models.ImageField(upload_to='produtos/')

    def __str__(self):
        return self.nome