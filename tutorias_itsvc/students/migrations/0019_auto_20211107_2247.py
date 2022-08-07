# Generated by Django 3.0.10 on 2021-11-07 22:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0018_auto_20211107_2207'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentjob',
            name='company_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='studentjob',
            name='schedule',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='studentscholarship',
            name='dependence_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
        migrations.AlterField(
            model_name='studentscholarship',
            name='institute_name',
            field=models.CharField(blank=True, max_length=150, null=True),
        ),
    ]
