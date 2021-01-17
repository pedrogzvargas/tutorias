from django.urls import path
from tutorias_itsvc.academy.views.api.v1.period import PeriodApi

app_name = "university"

urlpatterns = [
    path("period/", PeriodApi.as_view()),
]
