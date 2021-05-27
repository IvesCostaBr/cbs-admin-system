from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=80)

    def __str__(self):
        return str(self.description)
