from .profile import urlpatterns as profile_urlpatterns
from .academic_information import urlpatterns as academic_information_urlpatterns


urlpatterns = []
urlpatterns += profile_urlpatterns
urlpatterns += academic_information_urlpatterns


__all__ = [
    'urlpatterns',
]
