from django.db import models

class RegisterExtraHour(models.Model):
    reason = models.CharField(max_length=100)


    def __str__(self):
        return str(self.reason)