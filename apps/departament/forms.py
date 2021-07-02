from django import forms
from .models import Departament


class DepartamentsForm(forms.ModelForm):
        
    class Meta:
        model = Departament
        fields = '__all__'
        exclude = ['company']