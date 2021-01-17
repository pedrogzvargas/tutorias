from django.urls import path
from tutorias_itsvc.common.api.v1.views import (
    GenderView
)

app_name = "common"
urlpatterns = [
    path('genders/', GenderView.as_view()),
]
