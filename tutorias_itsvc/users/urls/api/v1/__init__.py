from .user import urlpatterns as user_urlpatterns
from .auth import urlpatterns as auth_urlpatterns
from .profile_image import urlpatterns as profile_image_urlpatterns
from .profile import urlpatterns as profile_urlpatterns


urlpatterns = []
urlpatterns += user_urlpatterns
urlpatterns += auth_urlpatterns
urlpatterns += profile_image_urlpatterns
urlpatterns += profile_urlpatterns

__all__ = [
    'urlpatterns',
]
