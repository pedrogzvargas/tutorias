from django.urls import path
from tutorias_itsvc.students.views.api.v1.load_data import StudentsLoadDataApi

app_name = "load_data"

urlpatterns = [
    path("load-students/", StudentsLoadDataApi.as_view()),
]
