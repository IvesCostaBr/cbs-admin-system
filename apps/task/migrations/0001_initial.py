# Generated by Django 3.2.3 on 2021-06-01 03:32

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('departament', '0002_alter_departament_id'),
        ('collaborator', '0005_alter_collaborator_total_horas'),
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40)),
                ('description', models.TextField(max_length=300)),
                ('date_creation', models.DateField(default=django.utils.timezone.now)),
                ('final_date', models.DateField(blank=True, null=True)),
                ('status', models.BooleanField(choices=[(0, 'Não Concluido'), (1, 'Concluido')], default=0)),
                ('collaborator', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='collaborator.collaborator')),
                ('departament', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='departament.departament')),
            ],
        ),
    ]