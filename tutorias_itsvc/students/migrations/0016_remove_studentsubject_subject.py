# Generated by Django 3.0.10 on 2021-10-18 00:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0015_auto_20211013_0105'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='studentsubject',
            name='subject',
        ),
    ]
