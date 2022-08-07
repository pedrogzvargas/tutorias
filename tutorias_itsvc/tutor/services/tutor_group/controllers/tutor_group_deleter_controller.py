from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.tutor.services.tutor_group import TutorGroupDeleterService


log = get_logger(__file__)


class TutorGroupDeleterController:
    def __init__(self, repository, response, service=None):
        self.__repository = repository
        self.__response = response
        self.__service = service or TutorGroupDeleterService(self.__repository)

    def __call__(self, advised_group_id):
        try:
            if not self.__repository.get(id=advised_group_id):
                raise Exception("No existe el registro")
            self.__service(advised_group_id)
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
            log.exception(f"Error in TutorGroupDeleterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
