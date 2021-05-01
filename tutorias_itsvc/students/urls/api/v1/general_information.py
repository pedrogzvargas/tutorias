from django.urls import path
from tutorias_itsvc.students.views.api.v1.general_information import GeneralInformationApi

app_name = "academic_information"

urlpatterns = [
    path("<int:user_id>/general-information/", GeneralInformationApi.as_view()),
]
