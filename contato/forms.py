from django import forms
from .models import Contato

class ContatoForm(forms.ModelForm):
    class Meta:
        model = Contato
        fields = ['nome_completo', 'email', 'telefone', 'melhor_horario', 'mensagem']
        widgets = {
            'mensagem': forms.Textarea(attrs={
                'rows': 5,
                'cols': 40,
                # 'class': 'form-control',
                'placeholder': 'Digite sua mensagem aqui...'
            }),
        }

    def clean(self):
        cleaned_data = super().clean()

        nome_completo = cleaned_data.get('nome_completo')
        telefone = cleaned_data.get('telefone')

        if nome_completo and nome_completo.strip() == "":
            self.add_error('nome_completo', "O nome completo é obrigatório.")

        if telefone and not telefone.isdigit():
            self.add_error('telefone', "O telefone deve conter apenas números.")

        return cleaned_data