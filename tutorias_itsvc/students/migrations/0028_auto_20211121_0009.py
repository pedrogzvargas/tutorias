# Generated by Django 3.0.10 on 2021-11-21 00:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0027_auto_20211119_0401'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='areaintegracion',
            options={'default_permissions': ()},
        ),
        migrations.AlterModelOptions(
            name='estadopsicofisiologico',
            options={'default_permissions': ()},
        ),
        migrations.CreateModel(
            name='CaracteristicasPersonales',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('p1', models.CharField(choices=[('No', 'No'), ('Poco', 'Poco'), ('Frecuente', 'Frecuente'), ('Mucho', 'Mucho')], max_length=20)),
                ('p2', models.CharField(choices=[('No', 'No'), ('Poco', 'Poco'), ('Frecuente', 'Frecuente'), ('Mucho', 'Mucho')], max_length=20)),
                ('p3', models.CharField(choices=[('No', 'No'), ('Poco', 'Poco'), ('Frecuente', 'Frecuente'), ('Mucho', 'Mucho')], max_length=20)),
                ('p4', models.CharField(choices=[('No', 'No'), ('Poco', 'Poco'), ('Frecuente', 'Frecuente'), ('Mucho', 'Mucho')], max_length=20)),
                ('p5', models.CharField(choices=[('No', 'No'), ('Poco', 'Poco'), ('Frecuente', 'Frecuente'), ('Mucho', 'Mucho')], max_length=20)),
                ('p6', models.CharField(choices=[('No', 'No'), ('Poco', 'Poco'), ('Frecuente', 'Frecuente'), ('Mucho', 'Mucho')], max_length=20)),
                ('p7', models.CharField(choices=[('No', 'No'), ('Poco', 'Poco'), ('Frecuente', 'Frecuente'), ('Mucho', 'Mucho')], max_length=20)),
                ('p8', models.CharField(choices=[('No', 'No'), ('Poco', 'Poco'), ('Frecuente', 'Frecuente'), ('Mucho', 'Mucho')], max_length=20)),
                ('p9', models.CharField(choices=[('No', 'No'), ('Poco', 'Poco'), ('Frecuente', 'Frecuente'), ('Mucho', 'Mucho')], max_length=20)),
                ('p10', models.CharField(choices=[('No', 'No'), ('Poco', 'Poco'), ('Frecuente', 'Frecuente'), ('Mucho', 'Mucho')], max_length=20)),
                ('p11', models.CharField(choices=[('No', 'No'), ('Poco', 'Poco'), ('Frecuente', 'Frecuente'), ('Mucho', 'Mucho')], max_length=20)),
                ('p12', models.CharField(choices=[('No', 'No'), ('Poco', 'Poco'), ('Frecuente', 'Frecuente'), ('Mucho', 'Mucho')], max_length=20)),
                ('p13', models.CharField(choices=[('No', 'No'), ('Poco', 'Poco'), ('Frecuente', 'Frecuente'), ('Mucho', 'Mucho')], max_length=20)),
                ('p14', models.CharField(choices=[('No', 'No'), ('Poco', 'Poco'), ('Frecuente', 'Frecuente'), ('Mucho', 'Mucho')], max_length=20)),
                ('p15', models.CharField(choices=[('No', 'No'), ('Poco', 'Poco'), ('Frecuente', 'Frecuente'), ('Mucho', 'Mucho')], max_length=20)),
                ('p16', models.CharField(choices=[('No', 'No'), ('Poco', 'Poco'), ('Frecuente', 'Frecuente'), ('Mucho', 'Mucho')], max_length=20)),
                ('p17', models.CharField(choices=[('No', 'No'), ('Poco', 'Poco'), ('Frecuente', 'Frecuente'), ('Mucho', 'Mucho')], max_length=20)),
                ('p18', models.CharField(choices=[('No', 'No'), ('Poco', 'Poco'), ('Frecuente', 'Frecuente'), ('Mucho', 'Mucho')], max_length=20)),
                ('p19', models.CharField(choices=[('No', 'No'), ('Poco', 'Poco'), ('Frecuente', 'Frecuente'), ('Mucho', 'Mucho')], max_length=20)),
                ('p20', models.CharField(choices=[('No', 'No'), ('Poco', 'Poco'), ('Frecuente', 'Frecuente'), ('Mucho', 'Mucho')], max_length=20)),
                ('p21', models.CharField(choices=[('No', 'No'), ('Poco', 'Poco'), ('Frecuente', 'Frecuente'), ('Mucho', 'Mucho')], max_length=20)),
                ('p22', models.CharField(choices=[('No', 'No'), ('Poco', 'Poco'), ('Frecuente', 'Frecuente'), ('Mucho', 'Mucho')], max_length=20)),
                ('p23', models.CharField(choices=[('No', 'No'), ('Poco', 'Poco'), ('Frecuente', 'Frecuente'), ('Mucho', 'Mucho')], max_length=20)),
                ('p24', models.CharField(choices=[('No', 'No'), ('Poco', 'Poco'), ('Frecuente', 'Frecuente'), ('Mucho', 'Mucho')], max_length=20)),
                ('p25', models.CharField(choices=[('No', 'No'), ('Poco', 'Poco'), ('Frecuente', 'Frecuente'), ('Mucho', 'Mucho')], max_length=20)),
                ('student', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='caracteristicas_personales', to='students.Student')),
            ],
            options={
                'default_permissions': (),
            },
        ),
    ]
