# Generated by Django 3.2.3 on 2021-07-02 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0013_alter_company_code_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='code_company',
            field=models.CharField(default='47946C', max_length=30),
        ),
    ]
