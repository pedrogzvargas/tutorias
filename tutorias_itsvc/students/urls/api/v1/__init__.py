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
from .job import urlpatterns as job_urlpatterns
from .scholarship import urlpatterns as scholarship_urlpatterns
from .estado_psicofisiologico import urlpatterns as estado_psicofisiologico_urlpatterns
from .area_integracion import urlpatterns as area_integracion_urlpatterns
from .caracteristicas_personales import urlpatterns as caracteristicas_personales_urlpatterns
from .area_psicopedagogica import urlpatterns as area_psicopedagogica_urlpatterns
from .organizacion_estudio import urlpatterns as organizacion_estudio_urlpatterns
from .tecnica_estudio import urlpatterns as tecnica_estudio_urlpatterns
from .motivacion_estudio import urlpatterns as motivacion_estudio_urlpatterns
from .estilo_aprendizaje import urlpatterns as estilo_aprendizaje_urlpatterns
from .interview_report import urlpatterns as interview_report_urlpatterns


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
urlpatterns += job_urlpatterns
urlpatterns += scholarship_urlpatterns
urlpatterns += estado_psicofisiologico_urlpatterns
urlpatterns += area_integracion_urlpatterns
urlpatterns += caracteristicas_personales_urlpatterns
urlpatterns += area_psicopedagogica_urlpatterns
urlpatterns += organizacion_estudio_urlpatterns
urlpatterns += tecnica_estudio_urlpatterns
urlpatterns += motivacion_estudio_urlpatterns
urlpatterns += estilo_aprendizaje_urlpatterns
urlpatterns += interview_report_urlpatterns


__all__ = [
    'urlpatterns',
]
