from django.urls import include, path
from tutorias_itsvc.common.urls.api.v1 import urlpatterns as common_urls
from tutorias_itsvc.students.urls.api.v1 import urlpatterns as student_urlpatterns
from tutorias_itsvc.users.urls.api.v1 import urlpatterns as user_urlpatterns
from tutorias_itsvc.academy.urls.api.v1 import urlpatterns as academy_urlpatterns
from tutorias_itsvc.tutor.urls.api.v1 import urlpatterns as tutor_urlpatterns
from tutorias_itsvc.courses.urls.api.v1 import urlpatterns as course_urlpatterns


app_name = "api"

urlpatterns = [
    # API base url
    path("common/", include(common_urls)),
    path("students/", include(student_urlpatterns)),
    path("users/", include(user_urlpatterns)),
    path("academy/", include(academy_urlpatterns)),
    path("tutor/", include(tutor_urlpatterns)),
    path("course/", include(course_urlpatterns)),
]

