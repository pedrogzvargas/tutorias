from django.urls import path
from tutorias_itsvc.students.views.api.v1.parent import ParentApi
from tutorias_itsvc.students.views.api.v1.parent import ParentAddressApi

app_name = "parent"

urlpatterns = [
    path("<int:student_id>/parent/<str:type>/", ParentApi.as_view()),
    path("<int:student_id>/parent/<str:type>/address/", ParentAddressApi.as_view()),
]
