# Generated by Django 3.0.10 on 2021-07-11 19:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0003_auto_20210711_1913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorsubject',
            old_name='period_number_subject',
            new_name='academic_subject',
        ),
    ]