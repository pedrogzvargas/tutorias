from django.urls import path
from tutorias_itsvc.students.views.api.v1.area_integracion import AreaIntegracionApi

app_name = "area_integracion"

urlpatterns = [
    path("<int:student_id>/area-integracion/", AreaIntegracionApi.as_view()),
]
