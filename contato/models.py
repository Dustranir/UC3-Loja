from django.db import models

class Contato(models.Model):
    HORA_CONTATO_CHOICES = [
        ('Manhã', 'Manhã'),
        ('Tarde', 'Tarde'),
        ('Noite', 'Noite'),
    ]

    nome_completo = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    telefone = models.CharField(max_length=11)
    melhor_horario = models.CharField(max_length=10, choices=HORA_CONTATO_CHOICES)
    mensagem = models.TextField(max_length=1024)

    def __str__(self):
        return f'{self.nome_completo} ({self.email})'