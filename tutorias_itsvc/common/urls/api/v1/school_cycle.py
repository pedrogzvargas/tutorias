from django.urls import path
from tutorias_itsvc.common.views.api.v1.school_cycle import SchoolCyclesApi

app_name = "school_cycle"

urlpatterns = [
    path("school-cycle/", SchoolCyclesApi.as_view()),
]
