from django.urls import path
from tutorias_itsvc.students.views.api.v1.motivacion_estudio import MotivacionEstudioApi

app_name = "motivacion_estudio"

urlpatterns = [
    path("<int:student_id>/motivacion-estudio/", MotivacionEstudioApi.as_view()),
]
