from django.urls import path
from tutorias_itsvc.tutor.views.api.v1.tutor_group import TutorGroupsApi
from tutorias_itsvc.tutor.views.api.v1.tutor_group import TutorGroupApi
from tutorias_itsvc.tutor.views.api.v1.tutor_group import TutorGroupDetailApi


app_name = "tutor_group"

urlpatterns = [
    path("group/", TutorGroupsApi.as_view()),
    path("group/<tutor_group_id>/", TutorGroupApi.as_view()),
    path("group/<tutor_group_id>/detail/", TutorGroupDetailApi.as_view()),
]
