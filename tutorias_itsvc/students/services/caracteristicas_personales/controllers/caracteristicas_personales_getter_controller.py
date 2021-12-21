from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.services.caracteristicas_personales import CaracteristicasPersonalesGetterService
from tutorias_itsvc.students.repositories import CaracteristicasPersonalesRepository

log = get_logger(__file__)


class CaracteristicasPersonalesGetterController:
    def __init__(self,
                 response,
                 serializer,
                 caracteristicas_personales_repository=None,
                 service=None):
        self.__response = response
        self.__serializer = serializer
        self.__caracteristicas_personales_repository = caracteristicas_personales_repository or CaracteristicasPersonalesRepository()
        self.__service = service or CaracteristicasPersonalesGetterService(
            repository=self.__caracteristicas_personales_repository,
        )

    def __call__(self, **kwargs):
        try:
            caracteristicas_personales = self.__service(**kwargs)
            if caracteristicas_personales:
                serializer_data = self.__serializer(caracteristicas_personales)
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
            log.exception(f"Error in CaracteristicasPersonalesGetterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
