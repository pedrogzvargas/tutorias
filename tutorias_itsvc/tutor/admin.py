from django.contrib import admin
from .models import Tutor
from .models import TutorGroup

# Register your models here.

admin.site.register(Tutor)
admin.site.register(TutorGroup)
