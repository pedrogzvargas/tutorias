# Generated by Django 3.0.10 on 2021-06-13 23:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0013_auto_20210517_0049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentinstitute',
            name='end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='studentinstitute',
            name='start_date',
            field=models.DateField(blank=True, null=True),
        ),
    ]