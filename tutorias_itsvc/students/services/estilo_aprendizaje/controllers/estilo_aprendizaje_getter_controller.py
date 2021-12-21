from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.students.services.estilo_aprendizaje import EstiloAprendizajeGetterService
from tutorias_itsvc.students.repositories import EstiloAprendizajeRepository
from tutorias_itsvc.students.repositories import StudentRepository

log = get_logger(__file__)


class EstiloAprendizajeGetterController:
    def __init__(self,
                 response,
                 serializer,
                 estilo_aprendizaje_repository=None,
                 student_repository=None,
                 service=None):
        self.__response = response
        self.__serializer = serializer
        self.__estilo_aprendizaje_repository = estilo_aprendizaje_repository or EstiloAprendizajeRepository()
        self.__student_repository = student_repository or StudentRepository()
        self.__service = service or EstiloAprendizajeGetterService(
            repository=self.__estilo_aprendizaje_repository
        )

    def __call__(self, **kwargs):
        try:
            motivacion_estudio = self.__service(**kwargs)
            if motivacion_estudio:
                serializer_data = self.__serializer(motivacion_estudio)
                response_data = dict(
                    success=True,
                    message="All Ok",
                    data=serializer_data,
                )
                http_status = status.HTTP_200_OK
            else:
                response_data = dict(
                    success=False,
                    message="Not Found",
                    data={},
                )
                http_status = status.HTTP_404_NOT_FOUND
            return self.__response(response_data, http_status=http_status)
        except Exception as err:
            log.exception(f"Error in EstiloAprendizajeGetterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
