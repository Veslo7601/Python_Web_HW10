# Generated by Django 5.0.6 on 2024-05-22 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('quoteapp', '0002_alter_autors_born_date_alter_autors_born_location_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='autors',
            name='description',
            field=models.CharField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='quotes',
            name='quote',
            field=models.CharField(max_length=512),
        ),
        migrations.AlterField(
            model_name='tag',
            name='name',
            field=models.CharField(max_length=64, unique=True),
        ),
    ]
