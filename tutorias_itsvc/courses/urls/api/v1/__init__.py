from .course import urlpatterns as course_urlpatterns
from .student_course import urlpatterns as student_course_urlpatterns


urlpatterns = []
urlpatterns += course_urlpatterns
urlpatterns += student_course_urlpatterns

__all__ = [
    "urlpatterns",
]
