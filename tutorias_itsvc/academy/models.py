from django.db import models


class Major(models.Model):
    name = models.CharField(max_length=200)
    acronym = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        default_permissions = ()
        db_table = "academy_major"
        verbose_name = 'Carrera'
        verbose_name_plural = 'Carreras'

    def __str__(self):
        return self.name


class University(models.Model):
    name = models.CharField(max_length=200)
    acronym = models.CharField(max_length=10)
    majors = models.ManyToManyField(Major, through='AcademicMajor', through_fields=('university', 'major'))
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        default_permissions = ()
        db_table = "academy_university"
        verbose_name = 'Universidad'
        verbose_name_plural = "Universidades"

    def __str__(self):
        return self.name


class AcademicMajor(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    major = models.ForeignKey(Major, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return f'{self.university.acronym} -- {self.major.name}'

    class Meta:
        default_permissions = ()
        db_table = "academy_academic_major"
        unique_together = ('university', 'major', )
        default_related_name = 'academy_major'
        verbose_name = 'Carrera academia'
        verbose_name_plural = "Carreras academia"


class Period(models.Model):
    name = models.CharField(max_length=100)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.name

    class Meta:
        default_permissions = ()
        db_table = "academy_period"
        verbose_name = 'Periodo academico'
        verbose_name_plural = "Periodos academicos"


class AcademicPeriod(models.Model):
    academic_major = models.ForeignKey(AcademicMajor, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, related_name='academic_period', on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.academic_major.university.name} -- {self.academic_major.major.name} -- {self.period.name}'

    class Meta:
        default_permissions = ()
        db_table = "academy_academic_period"
        unique_together = ('academic_major', 'period',)
        verbose_name = 'Periodo academia'
        verbose_name_plural = "Periodos academia"


class PeriodNumber(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=200)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        default_permissions = ()
        db_table = "academy_period_number"
        verbose_name = 'Número de periodo'
        verbose_name_plural = "Número de periodos"

    def __str__(self):
        return self.name


class AcademicPeriodNumber(models.Model):
    academic_period = models.ForeignKey(AcademicPeriod, on_delete=models.CASCADE)
    period_number = models.ForeignKey(PeriodNumber, related_name='academic_period_number', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        default_permissions = ()
        db_table = "academy_academic_period_number"
        verbose_name = 'Academia número de periodo'
        verbose_name_plural = "Academia número de periodos"

    def __str__(self):
        return f'{self.academic_period.academic_major.university.name} ' \
               f'-- {self.academic_period.academic_major.major.name} -- {self.period_number}'


class Group(models.Model):
    name = models.CharField(max_length=10)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        default_permissions = ()
        db_table = "academy_group"
        verbose_name = 'Grupo'
        verbose_name_plural = "Grupos"

    def __str__(self):
        return self.name


class AcademicGroup(models.Model):
    academic_period_number = models.ForeignKey(AcademicPeriodNumber, on_delete=models.CASCADE)
    group = models.ForeignKey(Group, related_name='academic_group', on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        default_permissions = ()
        db_table = "academy_academic_group"
        verbose_name = 'Academia grupo'
        verbose_name_plural = "Academia grupos"

    def __str__(self):
        return f'{self.academic_period_number.academic_period.academic_major.university.name} --' \
               f'{self.academic_period_number.academic_period.academic_major.major.name} -- ' \
               f'{self.academic_period_number.academic_period.period.name} --' \
               f'{self.academic_period_number.period_number} -- ' \
               f'{self.group.name}'


class Subject(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10)
    first_value = models.IntegerField(default=0)
    second_value = models.IntegerField(default=0)
    total_value = models.IntegerField(default=0)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        default_permissions = ()
        db_table = "academy_subject"
        verbose_name = 'Materia'
        verbose_name_plural = "Materias"

    def __str__(self):
        return self.name


class SubjectType(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        default_permissions = ()
        db_table = "academy_subject_type"
        verbose_name = 'Tipo de materia'
        verbose_name_plural = "Tipos de materias"

    def __str__(self):
        return self.name


class SubjectFailureMetric(models.Model):
    name = models.CharField(max_length=200)

    class Meta:
        default_permissions = ()
        db_table = "academy_subject_failure_metric"
        verbose_name = 'Métrica de reprobación'
        verbose_name_plural = "Métricas de reprobación"

    def __str__(self):
        return self.name


class AcademicSubject(models.Model):
    academic_period_number = models.ForeignKey(AcademicPeriodNumber, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        default_permissions = ()
        db_table = "academy_academic_subject"
        verbose_name = 'Academia materia'
        verbose_name_plural = "Academia materias"

    def __str__(self):
        return f'{self.academic_period_number.academic_period.academic_major.university.name} --' \
               f'{self.academic_period_number.academic_period.academic_major.major.name} -- ' \
               f'{self.academic_period_number.academic_period.period.name} -- ' \
               f'{self.academic_period_number.period_number.name} -- ' \
               f'{self.subject.name}'
