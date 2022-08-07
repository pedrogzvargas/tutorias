from django.urls import path
from tutorias_itsvc.common.views.api.v1.state import StatesApi

app_name = "state"

urlpatterns = [
    path("state/", StatesApi.as_view()),
]
