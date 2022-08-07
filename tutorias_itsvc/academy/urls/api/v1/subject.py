from django.urls import path
from tutorias_itsvc.academy.views.api.v1.subject import SubjectsApi

app_name = "subject"

urlpatterns = [
    path("subject/", SubjectsApi.as_view()),
]
