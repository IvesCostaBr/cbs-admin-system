# Generated by Django 3.2.3 on 2021-06-12 05:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('collaborator', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='collaborator',
            options={'permissions': (('gerente_geral', 'administrative functions in system.'), ('funcionario', 'user common is system'), ('lider_departament', 'lider in departaments'))},
        ),
    ]