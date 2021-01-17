# Generated by Django 3.0.10 on 2020-10-24 22:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import simple_history.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AcademicDegree',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Grado academico',
                'verbose_name_plural': 'Grados academicos',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Attitude',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Actitud',
                'verbose_name_plural': 'Actitudes',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Disability',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Deficiencia',
                'verbose_name_plural': 'Deficiencias',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Gender',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Genero',
                'verbose_name_plural': 'Generos',
                'db_table': 'common_gender',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='HomeStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Estatus de vivienda',
                'verbose_name_plural': 'Estatus de vivienda',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='HousingType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Tipo de vivienda',
                'verbose_name_plural': 'Tipos de viviendas',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('income', models.FloatField()),
                ('type', models.CharField(choices=[('main', 'Principal'), ('secondary', 'Secundario')], default='main', max_length=20)),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='MaritalStatus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Estado civil',
                'verbose_name_plural': 'Estados civiles',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=25)),
                ('type', models.CharField(choices=[('home_phone', 'Teléfono de Casa'), ('mobil_phone', 'Teléfono Celular')], max_length=15)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
            ],
            options={
                'verbose_name': 'Teléfono',
                'verbose_name_plural': 'Teléfonos',
                'db_table': 'common_phone',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='Relationship',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, null=True)),
            ],
            options={
                'verbose_name': 'Relación',
                'verbose_name_plural': 'Relaciones',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='SchoolCycle',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
            ],
            options={
                'verbose_name': 'Ciclo escolar',
                'verbose_name_plural': 'Ciclos escolares',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='State',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name': 'Estado',
                'verbose_name_plural': 'Estados',
                'db_table': 'common_state',
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='HistoricalPhone',
            fields=[
                ('id', models.IntegerField(auto_created=True, blank=True, db_index=True, verbose_name='ID')),
                ('number', models.CharField(max_length=25)),
                ('type', models.CharField(choices=[('home_phone', 'Teléfono de Casa'), ('mobil_phone', 'Teléfono Celular')], max_length=15)),
                ('created_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('updated_at', models.DateTimeField(blank=True, editable=False, null=True)),
                ('history_id', models.AutoField(primary_key=True, serialize=False)),
                ('history_date', models.DateTimeField()),
                ('history_change_reason', models.CharField(max_length=100, null=True)),
                ('history_type', models.CharField(choices=[('+', 'Created'), ('~', 'Changed'), ('-', 'Deleted')], max_length=1)),
                ('history_user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'historical Teléfono',
                'ordering': ('-history_date', '-history_id'),
                'get_latest_by': 'history_date',
            },
            bases=(simple_history.models.HistoricalChanges, models.Model),
        ),
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=200)),
                ('outdoor_number', models.CharField(max_length=50)),
                ('indoor_number', models.CharField(blank=True, max_length=50, null=True)),
                ('colony', models.CharField(max_length=200)),
                ('locality', models.CharField(max_length=200)),
                ('zip_code', models.CharField(max_length=5)),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.State')),
            ],
            options={
                'verbose_name': 'Dirección',
                'verbose_name_plural': 'Direcciónes',
                'default_permissions': (),
            },
        ),
    ]
