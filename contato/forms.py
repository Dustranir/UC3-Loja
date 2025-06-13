from django import forms
from .models import Contato

PERIODO = (
    ('Manhã', 'Manhã'),
    ('Tarde', 'Tarde'),
    ('Noite', 'Noite'),
)

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome_completo', 'email', 'telefone', 'melhor_horario', 'mensagem']

    def clean(self):
        cleaned_data = super().clean()

        if cleaned_data.get('nome_completo').strip() == "":
            self.add_error('nome_completo', "O nome completo é obrigatório.")

        telefone = cleaned_data.get('telefone')
        if telefone and not telefone.isdigit():
            self.add_error('telefone', "O telefone deve conter apenas números.")

        return cleaned_data
