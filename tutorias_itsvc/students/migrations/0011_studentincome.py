# Generated by Django 3.0.10 on 2021-05-16 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0010_auto_20210516_2126'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentIncome',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.FloatField(null=True)),
                ('family_income', models.FloatField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
