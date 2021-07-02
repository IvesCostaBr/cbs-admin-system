from django.forms import ModelForm
from django import forms
from .models import Collaborator


class CollaboratorForm(ModelForm):
    first_name = forms.CharField(max_length=30, label='Primerio Nome')
    last_name = forms.CharField(max_length=30, label='Sobrenome')
    email = forms.CharField(max_length=40, label='E-Mail')
    class Meta:
        model = Collaborator
        fields = ['first_name','last_name','email','cpf','profile_photo']

    def clean_email(self):
        email = self.cleaned_data['email']
        if Collaborator.objects.filter(user__username=email).exists():
            raise forms.ValidationError('Email já cadastrado, teste outro')
        return self.cleaned_data['email']
        

