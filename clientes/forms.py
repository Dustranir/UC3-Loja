from django import forms
from django.core.validators import RegexValidator
from .models import Cliente

ESTADOS = (
    ('RJ', 'Rio de Janeiro'),
    ('SP', 'São Paulo'),
    ('MG', 'Minas Gerais'),
    ('ES', 'Espírito Santo'),
    ('PR', 'Paraná'),
    ('BA', 'Bahia'),
    ('RS', 'Rio Grande do Sul'),
)

GENERO = (
    ('M', 'Masculino'),
    ('F', 'Feminino'),
    ('O', 'Outro'),
)

CONTATO = (
    ('C', 'Carta'),
    ('E', 'E-mail'),
    ('T', 'Telefone'),
    ('F', 'Fax'),
)

class ClienteForm(forms.ModelForm):
    cpf = forms.CharField(validators=[RegexValidator(r'^\d{11}$', message="CPF deve ter 11 números.")])
    telefone = forms.CharField(validators=[RegexValidator(r'^\d{11}$', message="Telefone deve ter 11 números.")])
    email = forms.EmailField()
    nome_usuario = forms.EmailField(label="Nome de usuário (mesmo e-mail)", required=True)
    senha = forms.CharField(min_length=8, max_length=8, widget=forms.PasswordInput)

    class Meta:
        model = Cliente
        fields = ['cpf', 'nome', 'endereco', 'telefone', 'estado', 'cidade', 'genero', 'contato', 'email', 'nome_usuario', 'senha']

    def clean(self):
        cleaned_data = super().clean()
        nome = cleaned_data.get("nome")

        if nome and (len(nome) < 10 or len(nome) > 25):
            self.add_error('nome', "O nome deve ter entre 10 e 25 caracteres.")

        # Garantir que nome de usuário == e-mail
        if cleaned_data.get('nome_usuario') != cleaned_data.get('email'):
            self.add_error('nome_usuario', "O nome de usuário deve ser igual ao e-mail informado.")

        return cleaned_data