# Generated by Django 3.2.3 on 2021-06-30 18:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0005_alter_company_code_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='code_company',
            field=models.CharField(default='9C2065', max_length=30),
        ),
    ]