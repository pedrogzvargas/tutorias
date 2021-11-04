from django.urls import path
from tutorias_itsvc.academy.views.api.v1.subject_type import SubjectTypesApi

app_name = "subject_type"

urlpatterns = [
    path("subject-type/", SubjectTypesApi.as_view()),
]
