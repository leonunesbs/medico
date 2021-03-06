# Generated by Django 2.2.23 on 2021-05-16 16:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Article',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField()),
                ('content', models.TextField()),
                ('status', models.CharField(choices=[('d', 'draft'), ('p', 'published')], max_length=1)),
                ('slug', models.SlugField(unique=True)),
                ('published_at', models.DateTimeField(auto_now_add=True)),
                ('last_update', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('slug', models.SlugField(unique=True)),
                ('position', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'Categories',
            },
        ),
    ]
