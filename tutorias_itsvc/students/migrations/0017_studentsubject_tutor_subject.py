# Generated by Django 3.0.10 on 2021-10-18 00:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tutor', '0007_remove_tutorsubject_type'),
        ('students', '0016_remove_studentsubject_subject'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsubject',
            name='tutor_subject',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='tutor.TutorSubject'),
        ),
    ]
