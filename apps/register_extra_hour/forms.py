from django import forms
from django.forms import widgets
from .models import RegisterExtraHour
from apps.collaborator.models import Collaborator


class HoraExtraForm(forms.ModelForm):
    def __init__(self, user, *args, **kwargs):
        super(HoraExtraForm, self).__init__(*args, **kwargs)
        self.fields['collaborator'].queryset = Collaborator.objects.filter(
            company=user.collaborator.company)
    
    class Meta:
        model = RegisterExtraHour
        fields = ('reason', 'collaborator', 'hours')