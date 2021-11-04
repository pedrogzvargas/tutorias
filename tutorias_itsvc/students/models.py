from django.db import models
from django.utils import timezone
from simple_history.models import HistoricalRecords
from tutorias_itsvc.users.models import User
from tutorias_itsvc.common.models import (
    Gender,
    Address,
    HousingType,
    HomeStatus,
    # Income,
    AcademicDegree,
    Phone,
    Disability,
    # MaritalStatus,
    SchoolCycle
)
from tutorias_itsvc.academy.models import (
    AcademicGroup,
    Subject,
    SubjectType,
    SubjectFailureMetric,
    PeriodNumber
)
from tutorias_itsvc.users.models import Sibling, Person
# from tutorias.students.model_permissions import student_permissions


class Student(models.Model):
    user = models.OneToOneField(User, related_name='student', on_delete=models.CASCADE)
    enrollment = models.CharField(max_length=10, unique=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return self.user.first_name

    class Meta:
        default_permissions = ()
        verbose_name = 'Estudiante'
        verbose_name_plural = 'Estudiantes'


class StudentAcademicInformation(models.Model):
    student = models.ForeignKey(Student, related_name="academic", on_delete=models.CASCADE)
    academic_information = models.ForeignKey(
        AcademicGroup,
        null=True,
        blank=True,
        on_delete=models.CASCADE
    )
    is_active = models.BooleanField(default=True)
    registered_at = models.DateTimeField(default=timezone.now)

    class Meta:
        default_permissions = ()
        verbose_name = 'Carrera de estudiante'
        verbose_name_plural = 'Carreras de estudiante'
        unique_together = ('student', 'is_active')


class StudentAddress(Address):
    student = models.OneToOneField(Student, related_name="address", on_delete=models.CASCADE)
    housing_type = models.ForeignKey(HousingType, on_delete=models.CASCADE)
    home_status = models.ForeignKey(HomeStatus, on_delete=models.CASCADE)
    home_status_description = models.CharField(max_length=255, null=True, blank=True)
    family_relationship = models.CharField(max_length=255)
    members = models.IntegerField()

    history = HistoricalRecords()

    class Meta:
        default_permissions = ()
        verbose_name = 'Dirección de estudiantes'
        verbose_name_plural = 'Direcciones de estudiantes'


class StudentPhone(Phone):
    student = models.ForeignKey(Student, related_name='student_phone', on_delete=models.CASCADE)
    # order = models.PositiveIntegerField(default=1)

    class Meta:
        default_permissions = ()


class StudentInstitute(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    institute_name = models.CharField(max_length=255)
    academic_degree = models.ForeignKey(AcademicDegree, on_delete=models.CASCADE)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)

    class Meta:
        default_permissions = ()


class StudentSibling(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    sibling = models.ForeignKey(Sibling, on_delete=models.CASCADE)

    class Meta:
        default_permissions = ()


# class StudentIncome(Income):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#
#     class Meta:
#         default_permissions = ()
#
#
# class FamilyIncome(Income):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#
#     class Meta:
#         default_permissions = ()

class StudentIncome(models.Model):
    student = models.OneToOneField(Student, related_name="income", on_delete=models.PROTECT)
    income = models.FloatField(null=True)
    family_income = models.FloatField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class StudentMedicalInformation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    disability = models.ForeignKey(Disability, on_delete=models.CASCADE)
    description = models.TextField(null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        default_permissions = ()


# class StudentMaritalStatus(models.Model):
#     student = models.ForeignKey(Student, on_delete=models.CASCADE)
#     marital_status = models.ForeignKey(MaritalStatus, on_delete=models.CASCADE)
#     description = models.TextField(null=True, blank=True)
#     created_at = models.DateTimeField(auto_now_add=True, null=True)
#     history = HistoricalRecords()
#
#     class Meta:
#         default_permissions = ()


class StudentParent(Person):
    FATHER = "father"
    MOTHER = "mother"
    PARENTS_TYPES = [
        (FATHER, "Padre"),
        (MOTHER, "Madre"),
    ]
    student = models.ForeignKey(Student, related_name='student_parent', on_delete=models.CASCADE)
    type = models.CharField(max_length=25, choices=PARENTS_TYPES)
    birth_date = models.DateField(null=True, blank=True)
    academic_degree = models.ForeignKey(AcademicDegree, on_delete=models.CASCADE)
    has_job = models.BooleanField(null=True, blank=True)
    workplace = models.CharField(max_length=255, null=True, blank=True)
    type_of_job = models.CharField(max_length=255, null=True, blank=True)
    profession_occupation = models.CharField(max_length=255, null=True, blank=True)
    is_alive = models.BooleanField(null=True, blank=True)
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.SET_NULL)

    class Meta:
        default_permissions = ()
        verbose_name = 'Padre'
        verbose_name_plural = 'Padres'
        unique_together = ('student', 'type')


class StudentSubject(models.Model):
    student = models.ForeignKey(Student, related_name='subject', on_delete=models.CASCADE)
    tutor_subject = models.ForeignKey("tutor.TutorSubject", on_delete=models.CASCADE, null=True)
    type = models.ForeignKey(SubjectType, on_delete=models.CASCADE)
    approved = models.BooleanField(null=True)
    final_score = models.FloatField(null=True)
    failure_metric = models.ForeignKey(SubjectFailureMetric, null=True, blank=True, on_delete=models.CASCADE)
    comment = models.TextField(null=True)
    school_cycle = models.ForeignKey(SchoolCycle, on_delete=models.CASCADE)
    unsubscribed = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        default_permissions = ()
        verbose_name = 'Materia de estudiante'
        verbose_name_plural = 'Materias de estudiante'
        # permissions = student_permissions

    def __str__(self):
        return f"{self.student.user.first_name}"
