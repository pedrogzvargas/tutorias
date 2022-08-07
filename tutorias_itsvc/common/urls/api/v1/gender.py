from django.urls import path
from tutorias_itsvc.common.views.api.v1.gender import GendersApi

app_name = "gender"

urlpatterns = [
    path("gender/", GendersApi.as_view()),
]
