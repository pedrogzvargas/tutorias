from .university import urlpatterns as university_urlpatterns
from .major import urlpatterns as major_urlpatterns
from .subject import urlpatterns as subject_urlpatterns


urlpatterns = []
urlpatterns += university_urlpatterns
urlpatterns += major_urlpatterns
urlpatterns += subject_urlpatterns


__all__ = [
    'urlpatterns',
]
