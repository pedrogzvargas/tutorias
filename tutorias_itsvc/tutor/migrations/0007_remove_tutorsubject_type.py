# Generated by Django 3.0.10 on 2021-07-29 03:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0006_auto_20210729_0300'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tutorsubject',
            name='type',
        ),
    ]