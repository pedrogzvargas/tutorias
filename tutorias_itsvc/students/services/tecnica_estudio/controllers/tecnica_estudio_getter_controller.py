from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.services.tecnica_estudio import TecnicaEstudioGetterService
from tutorias_itsvc.students.repositories import TecnicaEstudioRepository
from tutorias_itsvc.students.repositories import StudentRepository

log = get_logger(__file__)


class TecnicaEstudioGetterController:
    def __init__(self,
                 response,
                 serializer,
                 tecnica_estudio_repository=None,
                 student_repository=None,
                 service=None):
        self.__response = response
        self.__serializer = serializer
        self.__tecnica_estudio_repository = tecnica_estudio_repository or TecnicaEstudioRepository()
        self.__student_repository = student_repository or StudentRepository()
        self.__service = service or TecnicaEstudioGetterService(
            repository=self.__tecnica_estudio_repository
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
            log.exception(f"Error in TecnicaEstudioGetterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
