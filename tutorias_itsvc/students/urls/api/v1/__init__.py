from .profile import urlpatterns as profile_urlpatterns
from .academic_information import urlpatterns as academic_information_urlpatterns
from .institute import urlpatterns as institute_urlpatterns
from .general_information import urlpatterns as general_information_urlpatterns
from .medical_information import urlpatterns as medical_information_urlpatterns
from .address import urlpatterns as address_urlpatterns
from .parent import urlpatterns as parent_urlpatterns
from .student import urlpatterns as student_urlpatterns
from .personal_information import urlpatterns as personal_information_urlpatterns
from .phone import urlpatterns as phone_urlpatterns
from .income import urlpatterns as income_urlpatterns
from .sibling import urlpatterns as sibling_urlpatterns
from .subject import urlpatterns as subject_urlpatterns


urlpatterns = []
urlpatterns += profile_urlpatterns
urlpatterns += academic_information_urlpatterns
urlpatterns += institute_urlpatterns
urlpatterns += general_information_urlpatterns
urlpatterns += medical_information_urlpatterns
urlpatterns += address_urlpatterns
urlpatterns += parent_urlpatterns
urlpatterns += student_urlpatterns
urlpatterns += personal_information_urlpatterns
urlpatterns += phone_urlpatterns
urlpatterns += income_urlpatterns
urlpatterns += sibling_urlpatterns
urlpatterns += subject_urlpatterns


__all__ = [
    'urlpatterns',
]
