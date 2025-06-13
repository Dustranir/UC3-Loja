from django.db import models

class Fabricante(models.Model):
    codigo = models.AutoField(primary_key=True)
    nome = models.CharField(max_length=70)

    def __str__(self):
        return f'{self.nome} (Código: {self.codigo})'