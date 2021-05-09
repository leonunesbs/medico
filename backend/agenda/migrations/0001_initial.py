# Generated by Django 2.2.22 on 2021-05-09 16:25

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('colaboradores', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Agenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('horario', models.DateTimeField()),
                ('colaborador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='colaboradores.Colaborador')),
            ],
        ),
    ]
