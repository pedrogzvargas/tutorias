from django.urls import path
from tutorias_itsvc.common.views.api.v1.academic_degree import AcademicDegreesApi

app_name = "academic_degree"

urlpatterns = [
    path("academic-degree/", AcademicDegreesApi.as_view()),
]
