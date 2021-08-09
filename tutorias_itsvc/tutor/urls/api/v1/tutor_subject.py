from django.urls import path
from tutorias_itsvc.tutor.views.api.v1.tutor_subject import TutorSubjectsApi
from tutorias_itsvc.tutor.views.api.v1.tutor_subject import TutorSubjectApi
from tutorias_itsvc.tutor.views.api.v1.tutor_subject import TutorSubjectDetailApi


app_name = "tutor_subject"

urlpatterns = [
    path("subject/", TutorSubjectsApi.as_view()),
    path("subject/<int:tutor_subject_id>/", TutorSubjectApi.as_view()),
    path("subject/<int:tutor_subject_id>/detail/", TutorSubjectDetailApi.as_view()),
]
