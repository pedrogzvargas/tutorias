from django.urls import path
from tutorias_itsvc.students.views.api.v1.medical_information import MedicalInformationsApi
from tutorias_itsvc.students.views.api.v1.medical_information import MedicalInformationApi

app_name = "student_medical_information"

urlpatterns = [
    path("<int:student_id>/medical-information/", MedicalInformationsApi.as_view()),
    path("<int:student_id>/medical-information/<int:medical_information_id>/", MedicalInformationApi.as_view()),
]
