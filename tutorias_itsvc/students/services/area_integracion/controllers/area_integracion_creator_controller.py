from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.students.services.area_integracion import AreaIntegracionCreatorService
from tutorias_itsvc.students.repositories import AreaIntegracionRepository
from tutorias_itsvc.students.repositories import StudentRepository

log = get_logger(__file__)


class AreaIntegracionCreatorController:
    def __init__(self,
                 request,
                 response,
                 area_integracion_repository=None,
                 student_repository=None,
                 service=None):
        self.__request = request
        self.__response = response
        self.__area_integracion_repository = area_integracion_repository or AreaIntegracionRepository()
        self.__student_repository = student_repository or StudentRepository()
        self.__service = service or AreaIntegracionCreatorService(
            area_integracion_repository=self.__area_integracion_repository,
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
            return self.__response(response_data, http_status=status.HTTP_201_CREATED)
        except SerializerApiException as err:
            response_data = dict(
                success=False,
                message=f"{err}",
                errors=err.errors
            )
            return self.__response(response_data, http_status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            log.exception(f"Error in AreaIntegracionCreatorController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
