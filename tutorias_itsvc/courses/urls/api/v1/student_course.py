from django.urls import path
from tutorias_itsvc.courses.views.api.v1.course import StudentCourseApi

app_name = "course"

urlpatterns = [
    path("<int:student_id>/course/<course_id>/", StudentCourseApi.as_view()),
]
