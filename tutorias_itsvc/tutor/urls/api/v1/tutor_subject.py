from django.urls import path
from tutorias_itsvc.tutor.views.api.v1.tutor_subject import TaughtSubjectsApi
from tutorias_itsvc.tutor.views.api.v1.tutor_subject import TaughtSubjectApi
from tutorias_itsvc.tutor.views.api.v1.tutor_subject import TaughtSubjectDetailApi
from tutorias_itsvc.tutor.views.api.v1.tutor_subject import TutorSubjectsApi


app_name = "tutor_subject"

urlpatterns = [
    path("subject/", TaughtSubjectsApi.as_view()),
    path("subject/<int:taught_subject_id>/", TaughtSubjectApi.as_view()),
    path("subject/<int:taught_subject_id>/detail/", TaughtSubjectDetailApi.as_view()),
    path("<int:tutor_id>/subject/", TutorSubjectsApi.as_view()),
]
