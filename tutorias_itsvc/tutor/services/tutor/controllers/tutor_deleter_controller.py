from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.tutor.services.tutor import TutorDeleterService

log = get_logger(__file__)


class TutorDeleterController:
    def __init__(self, repository, response, service=None):
        self.__repository = repository
        self.__response = response
        self.__service = service or TutorDeleterService(self.__repository)

    def __call__(self, tutor_id):
        try:
            tutor = self.__repository.get(id=tutor_id)
            if tutor:
                self.__service(id=tutor_id)
                response_data = dict(
                    success=True,
                    message="All Ok",
                    data={},
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
            log.exception(f"Error in TutorDeleterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
