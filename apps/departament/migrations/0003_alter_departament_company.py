# Generated by Django 3.2.3 on 2021-05-29 04:05

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('company', '__first__'),
        ('departament', '0002_departament_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='departament',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='company.company'),
        ),
    ]