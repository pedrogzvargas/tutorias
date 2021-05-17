from django.urls import path
from tutorias_itsvc.students.views.api.v1.personal_information import PersonalInformationApi

app_name = "personal_information"

urlpatterns = [
    path("<int:student_id>/personal-information/", PersonalInformationApi.as_view()),
]
