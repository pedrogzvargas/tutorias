from django.urls import path
from tutorias_itsvc.students.views.api.v1.area_psicopedagogica import AreaPsicopedagogicaApi

app_name = "area_psicopedagogica"

urlpatterns = [
    path("<int:student_id>/area-psicopedagogica/", AreaPsicopedagogicaApi.as_view()),
]
