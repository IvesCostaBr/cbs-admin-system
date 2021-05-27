from django.db import models


class Collaborator(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)

    def __str__(self):
        return 'Collaborator Name:'+ str(self.first_name)