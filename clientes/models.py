from django.db import models

class Cliente(models.Model):
    ESTADO_CHOICES = [
        ('RJ', 'Rio de Janeiro'),
        ('SP', 'São Paulo'),
        ('MG', 'Minas Gerais'),
        ('ES', 'Espírito Santo'),
        ('PR', 'Paraná'),
        ('BA', 'Bahia'),
        ('RS', 'Rio Grande do Sul'),
    ]

    GENERO_CHOICES = [
        ('M', 'Masculino'),
        ('F', 'Feminino'),
        ('O', 'Outro'),
    ]

    CONTATO_CHOICES = [
        ('C', 'Carta'),
        ('E', 'E-mail'),
        ('T', 'Telefone'),
        ('F', 'Fax'),
    ]

    cpf = models.CharField(max_length=11, primary_key=True, unique=True)
    nome = models.CharField(max_length=70)
    endereco = models.CharField(max_length=100)
    telefone = models.CharField(max_length=11)
    estado = models.CharField(max_length=2, choices=ESTADO_CHOICES)
    cidade = models.CharField(max_length=50)
    genero = models.CharField(max_length=1, choices=GENERO_CHOICES)
    contato = models.CharField(max_length=1, choices=CONTATO_CHOICES)
    email = models.EmailField(max_length=100, unique=True)
    nome_usuario = models.CharField(max_length=100, unique=True)
    senha = models.CharField(max_length=256)
    estado_domicilio = models.CharField(max_length=2, choices=ESTADO_CHOICES)

def __str__(self):
    return f"CPF: {self.cpf} - Nome: {self.nome} - Username: {self.username}"