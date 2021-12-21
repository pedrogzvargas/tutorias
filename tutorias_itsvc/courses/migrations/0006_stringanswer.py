# Generated by Django 3.0.10 on 2021-11-14 15:46

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_auto_20211114_1528'),
    ]

    operations = [
        migrations.CreateModel(
            name='StringAnswer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('string_response', models.CharField(blank=True, max_length=255)),
                ('question', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='string_answer', to='courses.Question')),
            ],
            options={
                'verbose_name': 'Respuesta tipo cadena',
                'verbose_name_plural': 'Respuestas tipo cadena',
                'default_permissions': (),
            },
        ),
    ]