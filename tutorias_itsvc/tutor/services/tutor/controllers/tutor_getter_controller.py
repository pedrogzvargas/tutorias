from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.tutor.services.tutor import TutorGetterService

log = get_logger(__file__)


class TutorGetterController:

    def __init__(self, repository, serializer, response, service=None):
        self.__repository = repository
        self.__serializer = serializer
        self.__response = response
        self.__service = service or TutorGetterService(self.__repository)

    def __call__(self, **kwargs):
        try:
            tutor = self.__service(**kwargs)
            if tutor:
                serializer_data = self.__serializer(tutor)
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
            log.exception(f"Error in TutorGetterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
