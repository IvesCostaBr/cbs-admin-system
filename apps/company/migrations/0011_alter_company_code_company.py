# Generated by Django 3.2.3 on 2021-07-01 15:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0010_alter_company_code_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='code_company',
            field=models.CharField(default='44D23B', max_length=30),
        ),
    ]
