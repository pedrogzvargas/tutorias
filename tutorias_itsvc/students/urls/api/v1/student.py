from django.urls import path
from tutorias_itsvc.students.views.api.v1.student import StudentsApi

app_name = "student_profile"

urlpatterns = [
    path("", StudentsApi.as_view()),
]
