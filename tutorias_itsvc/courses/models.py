from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from tutorias_itsvc.students.models import Student


class Course(models.Model):
    name = models.CharField(max_length=200)
    slug_name = models.SlugField(max_length=250, default='')
    description = models.TextField(null=True, blank=True)
    is_active = models.BooleanField(default=True)
    start_date = models.DateTimeField(default=timezone.now)
    end_date = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def save(self, *args, **kwargs):
        self.slug_name = slugify(self.name)
        super(Course, self).save(*args, **kwargs)

    class Meta:
        default_permissions = ()
        verbose_name = 'Curso'
        verbose_name_plural = "Cursos"

    def __str__(self):
        return self.name


class Module(models.Model):
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        default_permissions = ()
        verbose_name = 'Modulo'
        verbose_name_plural = "Modulos"


class Questionnaire(models.Model):
    course = models.ForeignKey(Course, related_name="questionnaire", on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    module = models.ForeignKey(Module, null=True, blank=True, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        default_permissions = ()
        verbose_name = 'Cuestionario'
        verbose_name_plural = "Cuestionarios"

    def __str__(self):
        return self.name


# class CourseQuestionnaire(models.Model):
#     course = models.ForeignKey(Course, on_delete=models.CASCADE)
#     questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE)
#     created_at = models.DateTimeField(auto_now_add=True, null=True)
#     updated_at = models.DateTimeField(auto_now=True, null=True)
#
#     class Meta:
#         default_permissions = ()


class QuestionType(models.Model):
    type = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        default_permissions = ()
        verbose_name = 'Tipo de pregunta'
        verbose_name_plural = "Tipos de preguntas"

    def __str__(self):
        return self.type


class Question(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, related_name="question", on_delete=models.CASCADE)
    question = models.CharField(max_length=255)
    question_type = models.ForeignKey(QuestionType, on_delete=models.CASCADE)
    required = models.BooleanField(null=False, default=False)
    number = models.IntegerField()
    value = models.DecimalField(default=0.0, max_digits=5, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        default_permissions = ()
        verbose_name = 'Pregunta'
        verbose_name_plural = "Preguntas"
        ordering = ('number',)

    def __str__(self):
        return f"{self.questionnaire} - {self.question}"


class QuestionChoice(models.Model):
    question = models.ForeignKey(Question, related_name="choice", on_delete=models.CASCADE)
    choice = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.question.question} - {self.choice}"

    class Meta:
        default_permissions = ()
        verbose_name = 'Opcion de respuesta'
        verbose_name_plural = "Opciones de respuestas"


# class Answer(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice = models.ForeignKey(QuestionChoice, on_delete=models.CASCADE, null=True)
#     string_response = models.CharField(null=True, max_length=255, blank=True)
#     large_string_response = models.TextField(null=True, blank=True)
#     bool_response = models.BooleanField(null=True)
#
#     def __str__(self):
#         return f'{self.choice} - {self.string_response} - {self.bool_response}'
#
#     class Meta:
#         default_permissions = ()
#         verbose_name = 'Respuesta'
#         verbose_name_plural = "Respuestas"


class ChoiceAnswer(models.Model):
    question = models.ForeignKey(Question, related_name="choice_answer", on_delete=models.CASCADE)
    choice = models.ForeignKey(QuestionChoice, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f'{self.choice}'

    class Meta:
        default_permissions = ()
        verbose_name = 'Respuesta tipo opciones'
        verbose_name_plural = "Respuestas tipo opciones"


class StringAnswer(models.Model):
    question = models.ForeignKey(Question, related_name="string_answer", on_delete=models.CASCADE)
    response = models.CharField(max_length=255, blank=True)

    def __str__(self):
        return f'{self.response}'

    class Meta:
        default_permissions = ()
        verbose_name = 'Respuesta tipo cadena'
        verbose_name_plural = "Respuestas tipo cadena"


class TextAnswer(models.Model):
    question = models.ForeignKey(Question, related_name="text_answer", on_delete=models.CASCADE)
    response = models.TextField(null=True, blank=True)

    def __str__(self):
        return f'{self.response}'

    class Meta:
        default_permissions = ()
        verbose_name = 'Respuesta tipo texto'
        verbose_name_plural = "Respuestas tipo texto"


class BoolAnswer(models.Model):
    question = models.ForeignKey(Question, related_name="bool_answer", on_delete=models.CASCADE)
    response = models.BooleanField()

    def __str__(self):
        return f'{self.response}'

    class Meta:
        default_permissions = ()
        verbose_name = 'Respuesta tipo bool'
        verbose_name_plural = "Respuestas tipo bool"


class StudetCourse(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="student_course")
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="student_course")
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.student.user.first_name} - {self.course}"

    class Meta:
        default_permissions = ()
        verbose_name = 'Curso de estudiante'
        verbose_name_plural = "Curso de estudiante"
