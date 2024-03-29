# Generated by Django 3.0.10 on 2021-11-14 04:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0019_auto_20211107_2247'),
        ('courses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='questiontype',
            options={'default_permissions': (), 'verbose_name': 'Tipo de pregunta', 'verbose_name_plural': 'Tipos de preguntas'},
        ),
        migrations.AlterField(
            model_name='coursequestionnaire',
            name='course',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='questionnaire', to='courses.Course'),
        ),
        migrations.CreateModel(
            name='StudetCourse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_course', to='courses.Course')),
                ('student', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_course', to='students.Student')),
            ],
            options={
                'verbose_name': 'Curso de estudiante',
                'verbose_name_plural': 'Curso de estudiante',
                'default_permissions': (),
            },
        ),
    ]
