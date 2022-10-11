from django.urls import path
from tutorias_itsvc.students.views.api.v1.load_data import StudentsLoadDataApi
from tutorias_itsvc.students.views.api.v1.load_data import StudentsSubjectLoadDataApi

app_name = "load_data"

urlpatterns = [
    path("load-students/", StudentsLoadDataApi.as_view()),
    path("load-subjects/", StudentsSubjectLoadDataApi.as_view()),
]
