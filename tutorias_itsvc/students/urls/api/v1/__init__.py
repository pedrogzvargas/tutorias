from .profile import urlpatterns as profile_urlpatterns
from .academic_information import urlpatterns as academic_information_urlpatterns
from .institute import urlpatterns as institute_urlpatterns
from .general_information import urlpatterns as general_information_urlpatterns
from .medical_information import urlpatterns as medical_information_urlpatterns
from .address import urlpatterns as address_urlpatterns
from .parent import urlpatterns as parent_urlpatterns


urlpatterns = []
urlpatterns += profile_urlpatterns
urlpatterns += academic_information_urlpatterns
urlpatterns += institute_urlpatterns
urlpatterns += general_information_urlpatterns
urlpatterns += medical_information_urlpatterns
urlpatterns += address_urlpatterns
urlpatterns += parent_urlpatterns


__all__ = [
    'urlpatterns',
]
