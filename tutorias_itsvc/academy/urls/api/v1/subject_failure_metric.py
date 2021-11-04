from django.urls import path
from tutorias_itsvc.academy.views.api.v1.subject_failure_metric import SubjectFailureMetricsApi

app_name = "subject_failure_metric"

urlpatterns = [
    path("subject-failure-metric/", SubjectFailureMetricsApi.as_view()),
]
