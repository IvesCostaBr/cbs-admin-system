# Generated by Django 3.2.3 on 2021-07-03 04:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collaborator', '0005_collaboratormanager'),
    ]

    operations = [
        migrations.DeleteModel(
            name='CollaboratorManager',
        ),
    ]