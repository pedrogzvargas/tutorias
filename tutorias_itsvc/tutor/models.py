from django.db import models
from tutorias_itsvc.users.models import User
from tutorias_itsvc.academy.models import AcademicMajor, SubjectType, Subject, AcademicGroup
from tutorias_itsvc.common.models import SchoolCycle


class Tutor(models.Model):
    user = models.OneToOneField(User, related_name='tutor', on_delete=models.CASCADE)
    enrollment = models.CharField(max_length=20, unique=True)
    academic = models.ForeignKey(AcademicMajor, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"

    class Meta:
        default_permissions = ()
        permissions = ()
        verbose_name = 'Tutor'
        verbose_name_plural = 'Tutores'


class TutorSubject(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, on_delete=models.CASCADE)
    school_cycle = models.ForeignKey(SchoolCycle, on_delete=models.CASCADE)

    class Meta:
        default_permissions = ()


class TutorGroup(models.Model):
    tutor = models.ForeignKey(Tutor, on_delete=models.CASCADE)
    academic_group = models.ForeignKey(
        AcademicGroup,
        related_name='academic_group',
        on_delete=models.CASCADE
    )
    school_cycle = models.ForeignKey(SchoolCycle, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.tutor.user.first_name} {self.tutor.user.last_name}"

    class Meta:
        default_permissions = ()
