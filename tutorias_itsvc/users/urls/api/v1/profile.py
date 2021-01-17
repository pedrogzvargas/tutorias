from django.urls import path
from tutorias_itsvc.users.views.api.v1.user import ProfileApi

app_name = "profile"

urlpatterns = [
    path("<int:user_id>/profile/", ProfileApi.as_view()),
]
