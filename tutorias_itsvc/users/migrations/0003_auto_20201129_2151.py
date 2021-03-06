# Generated by Django 3.0.10 on 2020-11-29 21:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_academic_coordinator_doctor_emergencycontact_manager_person_personphone_profileimage_psychologist_si'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='academic',
            name='second_last_name',
        ),
        migrations.RemoveField(
            model_name='academic',
            name='second_name',
        ),
        migrations.RemoveField(
            model_name='coordinator',
            name='second_last_name',
        ),
        migrations.RemoveField(
            model_name='coordinator',
            name='second_name',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='second_last_name',
        ),
        migrations.RemoveField(
            model_name='doctor',
            name='second_name',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='second_last_name',
        ),
        migrations.RemoveField(
            model_name='manager',
            name='second_name',
        ),
        migrations.RemoveField(
            model_name='psychologist',
            name='second_last_name',
        ),
        migrations.RemoveField(
            model_name='psychologist',
            name='second_name',
        ),
        migrations.RemoveField(
            model_name='user',
            name='name',
        ),
        migrations.AddField(
            model_name='user',
            name='second_last_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Second Last Name of User'),
        ),
        migrations.AddField(
            model_name='user',
            name='second_name',
            field=models.CharField(blank=True, max_length=255, verbose_name='Second Name of User'),
        ),
    ]
