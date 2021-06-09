from django.forms import ModelForm
from django import forms
from django.forms.widgets import Widget
from .models import Collaborator


class CollaboratorForm(ModelForm):
    first_name = forms.CharField(label='First Name', 
    max_length=30,
    required=True,
    widget=forms.TextInput(attrs={
        'class':"validate",
        'placeholder':'Lirst name',
        
     }))
    last_name = forms.CharField(label='Last Name', 
    max_length=30, 
    required=True,
    widget=forms.TextInput(attrs={
        'class':"validate",
        'placeholder':'Last name',
        
     }))


    class Meta:
        model = Collaborator
        fields = ['first_name', 'last_name','profile_photo']
