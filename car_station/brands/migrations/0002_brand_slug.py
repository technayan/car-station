# Generated by Django 4.2.7 on 2023-12-18 19:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brands', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='brand',
            name='slug',
            field=models.SlugField(blank=True, null=True, unique=True),
        ),
    ]
