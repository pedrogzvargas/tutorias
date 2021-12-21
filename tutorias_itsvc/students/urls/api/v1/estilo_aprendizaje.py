from django.urls import path
from tutorias_itsvc.students.views.api.v1.estilo_aprendizaje import EstiloAprendizajeApi

app_name = "estilo_aprendizaje"

urlpatterns = [
    path("<int:student_id>/estilo-aprendizaje/", EstiloAprendizajeApi.as_view()),
]
