# Generated by Django 3.0.10 on 2021-07-10 22:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('academy', '0003_auto_20210510_0327'),
        ('common', '0003_auto_20210510_0327'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tutor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('second_name', models.CharField(max_length=100, null=True)),
                ('second_last_name', models.CharField(max_length=100, null=True)),
                ('enrollment', models.CharField(max_length=20, unique=True)),
                ('active', models.BooleanField(default=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('academic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.AcademicMajor')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='tutor', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Tutor',
                'verbose_name_plural': 'Tutores',
                'permissions': (),
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='TutorSubject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('period_number_subject', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.AcademicSubject')),
                ('school_cycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.SchoolCycle')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor.Tutor')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='academy.SubjectType')),
            ],
            options={
                'default_permissions': (),
            },
        ),
        migrations.CreateModel(
            name='TutorGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('group_information', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='group_information', to='academy.AcademicGroup')),
                ('school_cycle', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.SchoolCycle')),
                ('tutor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='tutor.Tutor')),
            ],
            options={
                'default_permissions': (),
            },
        ),
    ]
