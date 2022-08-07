from django.urls import path
from tutorias_itsvc.common.views.api.v1.housin_type import HousingsTypeApi

app_name = "housing_type"

urlpatterns = [
    path("housing-type/", HousingsTypeApi.as_view()),
]
