from django.urls import path
from tutorias_itsvc.students.views.api.v1.parent import ParentApi
from tutorias_itsvc.students.views.api.v1.parent import ParentAddressApi
from tutorias_itsvc.students.views.api.v1.parent import ParentPhonesApi
from tutorias_itsvc.students.views.api.v1.parent import ParentPhoneApi

app_name = "parent"

urlpatterns = [
    path("<int:student_id>/parent/<str:type>/", ParentApi.as_view()),
    path("<int:student_id>/parent/<str:type>/address/", ParentAddressApi.as_view()),
    path("<int:student_id>/parent/<str:type>/phone/", ParentPhonesApi.as_view()),
    path("<int:student_id>/parent/<str:type>/phone/<int:phone_id>/", ParentPhoneApi.as_view()),
]
