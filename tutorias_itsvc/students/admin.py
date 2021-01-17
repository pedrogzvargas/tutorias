from django.contrib import admin
from .models import Student, StudentAcademicInformation

# Register your models here.
admin.site.register(Student)
admin.site.register(StudentAcademicInformation)
