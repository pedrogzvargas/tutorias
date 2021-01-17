from django.urls import path
from tutorias_itsvc.users.api.v1.views import User, ProfileImage, Login

app_name = "users"
urlpatterns = [
    path("login/", view=Login.as_view(), name="login"),
    path("<int:user_id>/", view=User.as_view(), name="user"),
    path("<int:user_id>/profile-image/", view=ProfileImage.as_view(), name="profile_image"),
]
