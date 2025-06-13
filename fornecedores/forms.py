from django import forms
from .models import Fabricante

class FabricanteForm(forms.ModelForm):
    class Meta:
        model = Fabricante
        fields = ['codigo', 'nome']

    def clean_nome(self):
        nome = self.cleaned_data['nome']
        if nome.strip() == "":
            raise forms.ValidationError("O nome não pode ficar em branco.")
        return nome
