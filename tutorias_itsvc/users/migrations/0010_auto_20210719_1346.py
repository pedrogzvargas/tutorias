# Generated by Django 3.0.10 on 2021-07-19 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0009_auto_20210523_0348'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='second_last_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Second Last Name of User'),
        ),
        migrations.AlterField(
            model_name='user',
            name='second_name',
            field=models.CharField(blank=True, max_length=255, null=True, verbose_name='Second Name of User'),
        ),
    ]
