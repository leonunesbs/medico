# Generated by Django 2.2.23 on 2021-05-16 16:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('colaboradores', '0001_initial'),
        ('agenda', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='agenda',
            name='colaborador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='agendas', to='colaboradores.Colaborador'),
        ),
    ]
