from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.students.services.tecnica_estudio import TecnicaEstudioUpdaterService
from tutorias_itsvc.students.repositories import TecnicaEstudioRepository
from tutorias_itsvc.students.repositories import StudentRepository

log = get_logger(__file__)


class TecnicaEstudioUpdaterController:
    def __init__(self,
                 request,
                 response,
                 tecnica_estudio_repository=None,
                 student_repository=None,
                 service=None):
        self.__request = request
        self.__response = response
        self.__tecnica_estudio_repository = tecnica_estudio_repository or TecnicaEstudioRepository()
        self.__student_repository = student_repository or StudentRepository()
        self.__service = service or TecnicaEstudioUpdaterService(
            tecnica_estudio_repository=self.__tecnica_estudio_repository,
            student_repository=self.__student_repository
        )

    def __call__(self, student_id):
        try:
            fields = self.__request.get_data()
            self.__service(student_id=student_id, **fields)
            response_data = dict(
                success=True,
                message="All Ok",
                data={},
            )
            return self.__response(response_data, http_status=status.HTTP_200_OK)
        except SerializerApiException as err:
            response_data = dict(
                success=False,
                message=f"{err}",
                errors=err.errors
            )
            return self.__response(response_data, http_status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            log.exception(f"Error in TecnicaEstudioUpdaterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
