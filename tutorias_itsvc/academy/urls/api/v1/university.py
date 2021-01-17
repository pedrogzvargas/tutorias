from django.urls import path
from tutorias_itsvc.academy.views.api.v1.university import UniversitiesApi, UniversityApi
from tutorias_itsvc.academy.views.api.v1.major import AcademicMajorApi
from tutorias_itsvc.academy.views.api.v1.period import PeriodApi
from tutorias_itsvc.academy.views.api.v1.period_number import PeriodNumberApi
from tutorias_itsvc.academy.views.api.v1.group import GroupApi


app_name = "university"

urlpatterns = [
    path("university/", UniversitiesApi.as_view()),
    path("university/<int:university_id>/", UniversityApi.as_view()),
    path("university/<int:university_id>/major/", AcademicMajorApi.as_view()),
    path("university/<int:university_id>/major/<int:major_id>/period/", PeriodApi.as_view()),
    path("university/<int:university_id>/major/<int:major_id>/period/<int:period_id>/period-number/", PeriodNumberApi.as_view()),
    path("university/<int:university_id>/major/<int:major_id>/period/<int:period_id>/period-number/<int:period_number_id>/groups/", GroupApi.as_view()),
]
