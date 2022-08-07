from django.urls import path
from tutorias_itsvc.students.views.api.v1.sibling import SiblingsApi
from tutorias_itsvc.students.views.api.v1.sibling import SiblingApi

app_name = "student_sibling"

urlpatterns = [
    path("<int:student_id>/sibling/", SiblingsApi.as_view()),
    path("<int:student_id>/sibling/<int:sibling_id>/", SiblingApi.as_view()),
]
