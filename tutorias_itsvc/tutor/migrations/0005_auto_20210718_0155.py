# Generated by Django 3.0.10 on 2021-07-18 01:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0004_auto_20210711_1922'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutor',
            old_name='active',
            new_name='is_active',
        ),
    ]
