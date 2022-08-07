from django.urls import path
from tutorias_itsvc.students.views.api.v1.student import StudentsApi
from tutorias_itsvc.students.views.api.v1.student import StudentApi

app_name = "student_profile"

urlpatterns = [
    path("", StudentsApi.as_view()),
    path("<int:student_id>/", StudentApi.as_view()),
]
