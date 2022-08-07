from django.urls import path
from tutorias_itsvc.common.views.api.v1.marital_status import MaritalStatusesApi

app_name = "marital_status"

urlpatterns = [
    path("marital-status/", MaritalStatusesApi.as_view()),
]
