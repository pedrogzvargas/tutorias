# Generated by Django 3.0.10 on 2021-11-15 02:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0007_auto_20211114_1551'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='question',
            options={'default_permissions': (), 'ordering': ('number',), 'verbose_name': 'Pregunta', 'verbose_name_plural': 'Preguntas'},
        ),
        migrations.AddField(
            model_name='question',
            name='required',
            field=models.BooleanField(default=False),
        ),
    ]
