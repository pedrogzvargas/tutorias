from django.urls import path
from tutorias_itsvc.tutor.views.api.v1.tutor_group import AdvisedGroupsApi
from tutorias_itsvc.tutor.views.api.v1.tutor_group import AdvisedGroupApi
from tutorias_itsvc.tutor.views.api.v1.tutor_group import AdvisedGroupDetailApi
from tutorias_itsvc.tutor.views.api.v1.tutor_group import TutorGroupsApi


app_name = "tutor_group"

urlpatterns = [
    path("group/", AdvisedGroupsApi.as_view()),
    path("group/<advised_group_id>/", AdvisedGroupApi.as_view()),
    path("group/<advised_group_id>/detail/", AdvisedGroupDetailApi.as_view()),
    path("<tutor_id>/group/", TutorGroupsApi.as_view()),
]
