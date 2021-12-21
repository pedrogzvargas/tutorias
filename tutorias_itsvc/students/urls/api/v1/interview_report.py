from django.urls import path
from tutorias_itsvc.students.views.api.v1.interview import intreview_report
from tutorias_itsvc.students.views.api.v1.interview.interview_api import InterviewApi

app_name = "interview_report"

urlpatterns = [
    path("interview-report/", intreview_report.html_to_pdf_view),
    path("<int:student_id>/interview-report-api/", InterviewApi.as_view()),
]
