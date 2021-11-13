from django.urls import path
from tutorias_itsvc.students.views.api.v1.scholarship import ScholarshipApi

app_name = "scholarship"

urlpatterns = [
    path("<int:student_id>/scholarship/", ScholarshipApi.as_view()),
]
