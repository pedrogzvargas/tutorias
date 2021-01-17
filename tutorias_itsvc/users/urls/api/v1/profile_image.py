from django.urls import path
from tutorias_itsvc.users.views.api.v1.profile_image import ProfileImageApi

app_name = "profile_image"

urlpatterns = [
    path("<int:user_id>/profile-image/", ProfileImageApi.as_view()),
]
