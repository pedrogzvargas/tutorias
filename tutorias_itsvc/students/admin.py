from django.contrib import admin
from .models import Student, StudentAcademicInformation, StudentSubject

# Register your models here.
admin.site.register(Student)
admin.site.register(StudentAcademicInformation)
admin.site.register(StudentSubject)
