from django.contrib.auth.models import User
from apps.company.models import Company
from django.contrib.auth.forms import AuthenticationForm

from django import forms


class UserLoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(UserLoginForm, self).__init__(*args, **kwargs)

    username = forms.EmailField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': '', 'id': 'hello'}))
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            'placeholder':'Password',
            'id':'password-field',
            'type':'password',
        }
))


class RegisterUser(forms.Form):
    first_name = forms.CharField(required=True,
    label='Seu Nome',
    max_length=30,
    widget=forms.TextInput(attrs={
        'class':"validate",
        'placeholder':'Digite seu Nome',
        'class':'form-control',
     }))
     
    last_name = forms.CharField(label='Sobrenome', 
    max_length=30, 
    required=True,
    widget=forms.TextInput(attrs={
        'class':"validate",
        'placeholder':'Digite seu Sobrenome',
        'class':'form-control',
        
     }))
    email = forms.EmailField(max_length=50, widget=forms.EmailInput(attrs={
        'class':'form-control',
        'placeholder':'exemple@seuemail.com',
        }))
    password1 = forms.CharField(label="Senha",max_length=40,
    widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Digite uma senha',
        }))
    password2 = forms.CharField(label='Cofirme sua senha',max_length=40,
    widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Confirme sua senha',
        }))
    company_code = forms.CharField(label='Company Code',max_length=40,
    widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'Digite o Código da sua empresa.:',
        }))

    class Meta:
        pass
   
    def clean_email(self):
        email = self.cleaned_data['email']
        if User.objects.filter(username=email).exists():
            raise forms.ValidationError('Nome de Usuario já em uso!')
        return self.cleaned_data.get('email')
        
    def clean_company_code(self):
        code = self.cleaned_data['company_code']
        if not Company.objects.filter(code_company=code).exists():
            raise forms.ValidationError('Codigo de Empresa não encontrado')
        return self.cleaned_data.get('company_code')
