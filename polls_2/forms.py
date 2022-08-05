from django import forms


class LoginForm(forms.Form):
    username = forms.CharField(max_length=50)
    password = forms.CharField()
    remember_password = forms.BooleanField(initial=True)


# 1. Proporcionar uma abstracao para definir os inputs.
# 2. Ajudam a definir validacoes (como clean_<atributo>)
class Conversor(forms.Form):
    moeda_origin = forms.CharField(max_length=3)
    moeda_destino = forms.CharField(max_length=3)

    def clean_moeda_origin(self):
        valid_moedas = [
            "BRL",
            "COP",
            "ARS",
        ]
        dado_do_browser = self.cleaned_data['moeda_origin']
        if dado_do_browser not in valid_moedas:
            raise forms.ValidationError(f"Moeda {dado_do_browser} nao aceita")
        return dado_do_browser
from .models import Category
class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = '__all__'
        #exclude = (
        #    'category_id',
        #)



