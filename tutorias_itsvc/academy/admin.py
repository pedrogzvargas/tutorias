from django.contrib import admin
from .models import (
    University,
    Major,
    AcademicMajor,
    Period,
    AcademicPeriod,
    PeriodNumber,
    AcademicPeriodNumber,
    Group,
    Subject,
    SubjectFailureMetric,
    AcademicSubject,
    AcademicGroup,
)

# Register your models here.
admin.site.register(University)
admin.site.register(Major)
admin.site.register(AcademicMajor)
admin.site.register(Period)
admin.site.register(AcademicPeriod)
admin.site.register(PeriodNumber)
admin.site.register(AcademicPeriodNumber)
admin.site.register(Group)
admin.site.register(Subject)
admin.site.register(SubjectFailureMetric)
admin.site.register(AcademicSubject)
admin.site.register(AcademicGroup)
