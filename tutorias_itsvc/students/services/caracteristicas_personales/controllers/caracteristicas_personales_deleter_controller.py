from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.students.services.caracteristicas_personales import CaracteristicasPersonalesDeleterService
from tutorias_itsvc.students.repositories import CaracteristicasPersonalesRepository
from tutorias_itsvc.students.repositories import StudentRepository

log = get_logger(__file__)


class CaracteristicasPersonalesDeleterController:
    def __init__(self,
                 response,
                 caracteristicas_personales_repository=None,
                 student_repository=None,
                 service=None):
        self.__response = response
        self.__caracteristicas_personales_repository = caracteristicas_personales_repository or CaracteristicasPersonalesRepository()
        self.__student_repository = student_repository or StudentRepository()
        self.__service = service or CaracteristicasPersonalesDeleterService(
            caracteristicas_personales_repository=self.__caracteristicas_personales_repository,
            student_repository=self.__student_repository
        )

    def __call__(self, student_id):
        try:
            self.__service(student_id=student_id)
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
            log.exception(f"Error in CaracteristicasPersonalesDeleterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
