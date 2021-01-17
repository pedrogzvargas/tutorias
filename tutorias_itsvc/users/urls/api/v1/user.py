from django.urls import path
from tutorias_itsvc.users.views.api.v1.user import UserApi

app_name = "user"

urlpatterns = [
    path("<int:user_id>/", UserApi.as_view()),
]
