# Generated by Django 3.2.3 on 2021-05-30 17:23

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('register_extra_hour', '0004_remove_registerextrahour_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='registerextrahour',
            name='date',
            field=models.DateTimeField(auto_created=django.utils.timezone.now, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
