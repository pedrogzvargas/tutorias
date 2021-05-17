from django.urls import path
from tutorias_itsvc.students.views.api.v1.institute import InstitutesApi, InstituteApi

app_name = "student_institute"

urlpatterns = [
    path("<int:student_id>/institute/", InstitutesApi.as_view()),
    path("<int:student_id>/institute/<int:institute_id>/", InstituteApi.as_view()),
]
