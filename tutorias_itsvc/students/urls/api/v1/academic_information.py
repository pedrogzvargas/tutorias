from django.urls import path
from tutorias_itsvc.students.views.api.v1.academic_information import AcademicInformationApi

app_name = "academic_information"

urlpatterns = [
    path("<int:student_id>/academic-information/", AcademicInformationApi.as_view()),
]
