from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.students.services.area_integracion import AreaIntegracionGetterService
from tutorias_itsvc.students.repositories import AreaIntegracionRepository
from tutorias_itsvc.students.repositories import StudentRepository

log = get_logger(__file__)


class AreaIntegracionGetterController:
    def __init__(self,
                 response,
                 serializer,
                 area_integracion_repository=None,
                 student_repository=None,
                 service=None):
        self.__response = response
        self.__serializer = serializer
        self.__area_integracion_repository = area_integracion_repository or AreaIntegracionRepository()
        self.__student_repository = student_repository or StudentRepository()
        self.__service = service or AreaIntegracionGetterService(
            repository=self.__area_integracion_repository,
        )

    def __call__(self, **kwargs):
        try:
            area_integracion = self.__service(**kwargs)
            if area_integracion:
                serializer_data = self.__serializer(area_integracion)
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
            log.exception(f"Error in AreaIntegracionGetterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
