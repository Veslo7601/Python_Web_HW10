# Generated by Django 5.0.6 on 2024-05-21 18:53

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Autors',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32, unique=True)),
                ('born_date', models.CharField(max_length=32)),
                ('born_location', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Quotes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quote', models.CharField(max_length=126)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='quoteapp.autors')),
                ('tags', models.ManyToManyField(to='quoteapp.tag')),
            ],
        ),
    ]
