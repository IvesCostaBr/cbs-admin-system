# Generated by Django 3.2.3 on 2021-05-30 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('collaborator', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='collaborator',
            name='total_horas',
            field=models.DecimalField(decimal_places=3, default=None, max_digits=5),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='collaborator',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
