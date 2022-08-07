from django.urls import path
from tutorias_itsvc.common.views.api.v1.home_status import HomesStatusApi

app_name = "home_status"

urlpatterns = [
    path("home-status/", HomesStatusApi.as_view()),
]
