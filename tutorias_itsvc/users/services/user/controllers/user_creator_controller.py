from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.users.services.user import UserCreatorService

log = get_logger(__file__)


class UserCreatorController:
    def __init__(self, request, repository, response, creator_service=None):
        self.__request = request
        self.__repository = repository
        self.__response = response
        self.__creator_service = creator_service or UserCreatorService(self.__repository)

    def __call__(self):
        try:
            fields = self.__request.get_data()
            self.__creator_service(**fields)
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
            log.exception(f"Error in UserCreatorController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",

            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
