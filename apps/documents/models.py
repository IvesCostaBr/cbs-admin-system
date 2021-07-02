from django.db import models
from apps.collaborator.models import Collaborator

#TODO:Blan True e Null True serão removidos em produção.
class Document(models.Model):
    description = models.CharField(max_length=80)
    #Não faz sentido documento está em collaborator, pois dessa forma 1 documento poderia pertencer a varios collaborator.
    owner = models.ForeignKey(Collaborator, on_delete=models.SET_NULL, null=True, blank=True)
    file = models.FileField(upload_to='uploads/%Y/%m/%d/', null=True, blank=True)

    
    
    def __str__(self):
        return str(self.description)
