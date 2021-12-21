# Generated by Django 3.0.10 on 2021-11-21 03:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0028_auto_20211121_0009'),
    ]

    operations = [
        migrations.CreateModel(
            name='AreaPsicopedagogica',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p1', models.TextField()),
                ('p2', models.BooleanField()),
                ('p3', models.CharField(choices=[('Económicos', 'Económicos'), ('Salud', 'Salud'), ('Familiares', 'Familiares'), ('Sociales', 'Sociales')], max_length=20)),
                ('p4', models.CharField(choices=[('Bueno', 'Bueno'), ('Regular', 'Regular'), ('Malo', 'Malo')], max_length=20)),
                ('p5', models.TextField()),
                ('p6', models.TextField()),
                ('p7', models.FloatField()),
                ('p8', models.BooleanField()),
                ('p8_1', models.IntegerField(blank=True, null=True)),
                ('p9', models.TextField()),
                ('p10', models.TextField()),
                ('p11', models.TextField()),
                ('p12', models.TextField()),
                ('p13', models.TextField()),
                ('p14', models.TextField()),
                ('p15', models.TextField()),
                ('p16', models.TextField()),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='area_psicopedagogica', to='students.Student')),
            ],
        ),
    ]