from .tutor import urlpatterns as tutor_urlpatterns
from .tutor_group import urlpatterns as tutor_group_urlpatterns
from .tutor_subject import urlpatterns as tutor_subject_urlpatterns

urlpatterns = []
urlpatterns += tutor_urlpatterns
urlpatterns += tutor_group_urlpatterns
urlpatterns += tutor_subject_urlpatterns


__all__ = [
    'urlpatterns',
]
