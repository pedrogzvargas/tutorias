from django.urls import path
from tutorias_itsvc.students.views.api.v1.phone import PhonesApi
from tutorias_itsvc.students.views.api.v1.phone import PhoneApi
from tutorias_itsvc.students.views.api.v1.phone import MobilePhoneApi
from tutorias_itsvc.students.views.api.v1.phone import HomePhoneApi

app_name = "phone"

urlpatterns = [
    path("<int:student_id>/phone/", PhonesApi.as_view()),
    path("<int:student_id>/phone/<int:phone_id>/", PhoneApi.as_view()),
    path("<int:student_id>/phone/mobile/", MobilePhoneApi.as_view()),
    path("<int:student_id>/phone/home/", HomePhoneApi.as_view()),
]
