from django.urls import path
from tutorias_itsvc.students.views.api.v1.subject import SubjectApi
from tutorias_itsvc.students.views.api.v1.subject import SubjectsApi
from tutorias_itsvc.students.views.api.v1.subject import SubjectsDetailApi

app_name = "student_subject"

urlpatterns = [
    path("<int:student_id>/subject/", SubjectsApi.as_view()),
    path("<int:student_id>/subject/<int:subject_id>/", SubjectApi.as_view()),
    path("<int:student_id>/subject-details/", SubjectsDetailApi.as_view()),
]
