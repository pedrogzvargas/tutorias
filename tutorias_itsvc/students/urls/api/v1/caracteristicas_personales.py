from django.urls import path
from tutorias_itsvc.students.views.api.v1.caracteristicas_personales import CaracteristicasPersonalesApi

app_name = "caracteristicas_personales"

urlpatterns = [
    path("<int:student_id>/caracteristicas-personales/", CaracteristicasPersonalesApi.as_view()),
]
