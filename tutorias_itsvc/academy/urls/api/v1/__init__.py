from .university import urlpatterns as university_urlpatterns
from .major import urlpatterns as major_urlpatterns
from .subject import urlpatterns as subject_urlpatterns
from .subject_type import urlpatterns as subject_type_urlpatterns
from .subject_failure_metric import urlpatterns as subject_failure_metric_urlpatterns


urlpatterns = []
urlpatterns += university_urlpatterns
urlpatterns += major_urlpatterns
urlpatterns += subject_urlpatterns
urlpatterns += subject_type_urlpatterns
urlpatterns += subject_failure_metric_urlpatterns


__all__ = [
    'urlpatterns',
]
