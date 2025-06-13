from django.db import models
from clientes.models import Cliente
from produtos.models import Produto
from django.utils import timezone

class Venda(models.Model):
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    data_venda = models.DateTimeField(default=timezone.now)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"Venda de {self.produto.nome} para {self.cliente.nome} em {self.data_venda.strftime('%d/%m/%Y')}"