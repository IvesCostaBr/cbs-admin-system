# Generated by Django 3.2.3 on 2021-05-30 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('company', '0004_alter_company_gerente'),
    ]

    operations = [
        migrations.AddField(
            model_name='company',
            name='cidade',
            field=models.CharField(default='RIO BRANCO', max_length=30),
            preserve_default=False,
        ),
    ]