from django.urls import path
from tutorias_itsvc.students.views.api.v1.tecnica_estudio import TecnicaEstudioApi

app_name = "tecnica_estudio"

urlpatterns = [
    path("<int:student_id>/tecnica-estudio/", TecnicaEstudioApi.as_view()),
]
