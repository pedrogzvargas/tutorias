from django.urls import path
from tutorias_itsvc.students.views.api.v1.address import AddressApi

app_name = "student_address"

urlpatterns = [
    path("<int:student_id>/address/", AddressApi.as_view()),
]
