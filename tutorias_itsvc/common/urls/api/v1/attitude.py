from django.urls import path
from tutorias_itsvc.common.views.api.v1.attitude import AttitudesApi

app_name = "attitude"

urlpatterns = [
    path("attitude/", AttitudesApi.as_view()),
]
