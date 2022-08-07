from django.urls import path
from tutorias_itsvc.students.views.api.v1.organizacion_estudio import OrganizacionEstudioApi

app_name = "organizacion_estudio"

urlpatterns = [
    path("<int:student_id>/organizacion-estudio/", OrganizacionEstudioApi.as_view()),
]
