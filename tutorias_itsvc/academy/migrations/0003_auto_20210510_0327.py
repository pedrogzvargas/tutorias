# Generated by Django 3.0.10 on 2021-05-10 03:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('academy', '0002_auto_20201129_1910'),
    ]

    operations = [
        migrations.AlterField(
            model_name='academicgroup',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='academic_group', to='academy.Group'),
        ),
        migrations.AlterField(
            model_name='academicperiod',
            name='period',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='academic_period', to='academy.Period'),
        ),
        migrations.AlterField(
            model_name='academicperiodnumber',
            name='period_number',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='academic_period_number', to='academy.PeriodNumber'),
        ),
    ]