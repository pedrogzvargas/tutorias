from django.urls import path
from tutorias_itsvc.common.views.api.v1.disability import DisabilitiesApi

app_name = "disability"

urlpatterns = [
    path("disability/", DisabilitiesApi.as_view()),
]
