from django.urls import path
from tutorias_itsvc.common.views.api.v1.relationship import RelationshipsApi

app_name = "relationship"

urlpatterns = [
    path("relationship/", RelationshipsApi.as_view()),
]
