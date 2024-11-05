from django import forms
from .models import Conta, Transacao, Categoria

class ContaForm(forms.ModelForm):
    class Meta:
        model = Conta
        fields = ['nome', 'tipo']


class TransacaoForm(forms.ModelForm):
    class Meta:
        model = Transacao
        fields = ['conta', 'data', 'categoria', 'valor']  # Adicione 'conta' aqui

    # Adicionando uma opção para o campo conta
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(TransacaoForm, self).__init__(*args, **kwargs)
        if user:
            self.fields['conta'].queryset = Conta.objects.filter(usuario=user)
           # self.fields['categoria'].queryset = Categoria.objects.all()

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['tipo', 'nome']  # Inclua os campos que deseja no formulário