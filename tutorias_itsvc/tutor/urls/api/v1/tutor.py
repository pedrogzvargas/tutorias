from django.urls import path
from tutorias_itsvc.tutor.views.api.v1.tutor import TutorsApi
from tutorias_itsvc.tutor.views.api.v1.tutor import TutorApi


app_name = "tutor"

urlpatterns = [
    path("", TutorsApi.as_view()),
    path("<int:tutor_id>/", TutorApi.as_view()),
]
