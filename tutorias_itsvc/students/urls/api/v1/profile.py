from django.urls import path
from tutorias_itsvc.students.views.api.v1.profile import ProfileApi

app_name = "student_profile"

urlpatterns = [
    path("<int:student_id>/profile/", ProfileApi.as_view()),
]
