from django.urls import path
from tutorias_itsvc.users.views.api.v1.auth import LoginApi

app_name = "auth"

urlpatterns = [
    path("login/", LoginApi.as_view()),
]
