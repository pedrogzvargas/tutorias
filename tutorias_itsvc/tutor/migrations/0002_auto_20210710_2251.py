# Generated by Django 3.0.10 on 2021-07-10 22:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutor',
            name='second_last_name',
        ),
        migrations.RemoveField(
            model_name='tutor',
            name='second_name',
        ),
    ]
