# Generated by Django 3.0.10 on 2021-04-02 21:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0002_auto_20201024_2246'),
        ('users', '0005_auto_20210401_2129'),
    ]

    operations = [
        migrations.AddField(
            model_name='personalinformation',
            name='marital_status',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='common.MaritalStatus'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='personalinformation',
            name='marital_status_description',
            field=models.TextField(blank=True, null=True),
        ),
    ]
