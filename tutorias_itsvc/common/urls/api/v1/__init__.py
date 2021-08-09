from .gender import urlpatterns as gender_urlpatterns
from .marital_status import urlpatterns as marital_status_urlpatterns
from .academic_degree import urlpatterns as academic_degree_urlpatterns
from .disability import urlpatterns as disability_urlpatterns
from .state import urlpatterns as state_urlpatterns
from .home_status import urlpatterns as home_status_urlpatterns
from .housing_type import urlpatterns as housing_type_urlpatterns
from .attitude import urlpatterns as attitude_urlpatterns
from .relationship import urlpatterns as relationship_urlpatterns
from .school_cycle import urlpatterns as school_cycle_urlpatterns

urlpatterns = []
urlpatterns += gender_urlpatterns
urlpatterns += marital_status_urlpatterns
urlpatterns += academic_degree_urlpatterns
urlpatterns += disability_urlpatterns
urlpatterns += state_urlpatterns
urlpatterns += home_status_urlpatterns
urlpatterns += housing_type_urlpatterns
urlpatterns += attitude_urlpatterns
urlpatterns += relationship_urlpatterns
urlpatterns += school_cycle_urlpatterns


__all__ = [
    'urlpatterns',
]
