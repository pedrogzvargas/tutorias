from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.repositories import EstadoPsicofisiologicoRepository
from tutorias_itsvc.students.services.estado_psicofisiologico import EstadoPsicofisiologicoGetterService

log = get_logger(__file__)


class EstadoPsicofisiologicoGetterController:
    def __init__(self, response, serializer, estado_psicofisiologico_repository=None, getter_service=None):
        self.__response = response
        self.__serializer = serializer
        self.__estado_psicofisiologico_repository = estado_psicofisiologico_repository or EstadoPsicofisiologicoRepository()
        self.__service = getter_service or EstadoPsicofisiologicoGetterService(self.__estado_psicofisiologico_repository)

    def __call__(self, **kwargs):
        try:
            estado_psicofisiologico = self.__service(**kwargs)
            if estado_psicofisiologico:
                serializer_data = self.__serializer(estado_psicofisiologico)
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
            log.exception(f"Error in EstadoPsicofisiologicoGetterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
