from django.urls import path
from tutorias_itsvc.students.views.api.v1.estado_psicofisiologico import EstadoPsicofisiologicoApi

app_name = "estado_psicofisiologico"

urlpatterns = [
    path("<int:student_id>/estado-psicofisiologico/", EstadoPsicofisiologicoApi.as_view()),
]
