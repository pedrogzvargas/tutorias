from django.urls import path
from tutorias_itsvc.students.views.api.v1.job import JobApi

app_name = "job"

urlpatterns = [
    path("<int:student_id>/job/", JobApi.as_view()),
]
