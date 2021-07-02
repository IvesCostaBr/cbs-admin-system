from apps.departament.models import Departament
from django import forms
from .models import Task
from apps.collaborator.models import Collaborator
from apps.departament.models import Departament

class TaskForm(forms.ModelForm):
    def __init__(self, company_obj ,*args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['departament'].queryset = Departament.objects.filter(
            company=company_obj)
        self.fields['collaborator'].queryset = Collaborator.objects.filter(
            company=company_obj
        )

    class Meta:
        model = Task
        fields = '__all__'
        labels = {
            "departament":"Setores",
            "collaborator":"Funcionario",
            "title": "Titulo",
            "description": "Descrição da Tarefa",
            "date_creatin": "Data de Criação",
            "final_date": "Date de Entrega",
            "file_task": "Arquivo em anexo"
            
        }
        exclude = ['company', 'status']


class UploadFileForm(forms.Form):
    file = forms.FileField(label="Arquivos")