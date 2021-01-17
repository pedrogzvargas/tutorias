from .university import urlpatterns as university_urlpatterns
from .major import urlpatterns as major_urlpatterns


urlpatterns = []
urlpatterns += university_urlpatterns
urlpatterns += major_urlpatterns


__all__ = [
    'urlpatterns',
]
