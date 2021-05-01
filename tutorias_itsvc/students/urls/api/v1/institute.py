from django.urls import path
from tutorias_itsvc.students.views.api.v1.institute import InstitutesApi, InstituteApi

app_name = "student_institute"

urlpatterns = [
    path("institute/", InstitutesApi.as_view()),
    path("institute/<int:institute_id>/", InstituteApi.as_view()),
]
