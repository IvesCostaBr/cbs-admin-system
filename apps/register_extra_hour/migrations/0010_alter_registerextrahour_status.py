# Generated by Django 3.2.3 on 2021-07-02 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register_extra_hour', '0009_alter_registerextrahour_hours'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerextrahour',
            name='status',
            field=models.BooleanField(choices=[(False, 'N/Disponivel'), (True, 'Disponivel')], default=False),
        ),
    ]