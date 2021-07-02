# Generated by Django 3.2.3 on 2021-06-16 23:09

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('collaborator', '0003_alter_collaborator_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaborator',
            name='cpf',
            field=models.CharField(blank=True, max_length=14, null=True),
        ),
        migrations.AlterUniqueTogether(
            name='collaborator',
            unique_together={('user', 'cpf')},
        ),
        migrations.RemoveField(
            model_name='collaborator',
            name='first_name',
        ),
        migrations.RemoveField(
            model_name='collaborator',
            name='last_name',
        ),
    ]
