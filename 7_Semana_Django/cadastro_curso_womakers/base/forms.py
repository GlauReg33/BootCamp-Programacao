from django import forms
from base.models import cadastro

class CadastroForm(forms.ModelForm):
    class Meta:
        model = cadastro
        fields = ['nome', 'email','senha']
        widgets = {'senha': forms.PasswordInput()}
   