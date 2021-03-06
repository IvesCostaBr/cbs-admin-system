# Generated by Django 3.2.3 on 2021-07-01 14:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('collaborator', '0004_auto_20210616_2009'),
        ('register_extra_hour', '0005_alter_registerpoint_collaborator'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registerpoint',
            name='collaborator',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='collaborator.collaborator'),
        ),
        migrations.AlterField(
            model_name='registerpoint',
            name='date_logout',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
