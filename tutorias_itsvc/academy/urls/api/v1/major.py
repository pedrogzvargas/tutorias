from django.urls import path
from tutorias_itsvc.academy.views.api.v1.major import MajorsApi, MajorApi

app_name = "university"

urlpatterns = [
    path("major/", MajorsApi.as_view()),
    path("major/<int:major_id>/", MajorApi.as_view()),
]
