# Generated by Django 3.2.3 on 2021-06-21 15:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='code_company',
            field=models.CharField(default='42D6C7', max_length=30),
        ),
        migrations.AlterUniqueTogether(
            name='company',
            unique_together={('cnpj', 'code_company')},
        ),
    ]
