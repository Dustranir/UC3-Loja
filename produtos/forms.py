from django import forms
from .models import Produto

CORES = (
    ('Azul', 'Azul'),
    ('Vermelho', 'Vermelho'),
    ('Verde', 'Verde'),
    ('Amarelo', 'Amarelo'),
    ('Branco', 'Branco'),
    ('Preto', 'Preto'),
    ('Marrom', 'Marrom'),
)

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['codigo', 'nome', 'preco_compra', 'preco_venda', 'cor', 'data_fabricacao','descricao', 'imagem']

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if nome.strip() == "":
            raise forms.ValidationError("O nome não pode ficar em branco.")
        return nome
