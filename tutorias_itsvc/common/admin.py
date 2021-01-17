from django.contrib import admin
from .models import (
    Relationship,
    Phone,
    Gender,
    State,
    Disability,
    MaritalStatus,
    HousingType,
    HomeStatus,
    AcademicDegree,
    Address,
    Attitude,
    Income,
    SchoolCycle
)

# Register your models here.
admin.site.register(Relationship)
admin.site.register(Phone)
admin.site.register(Gender)
admin.site.register(State)
admin.site.register(Disability)
admin.site.register(MaritalStatus)
admin.site.register(HousingType)
admin.site.register(HomeStatus)
admin.site.register(AcademicDegree)
admin.site.register(Address)
admin.site.register(Attitude)
admin.site.register(Income)
admin.site.register(SchoolCycle)
