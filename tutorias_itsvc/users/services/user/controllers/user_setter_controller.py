from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.users.services.user import UserSetterService

log = get_logger(__file__)


class UserSetterController:
    def __init__(self, request, repository, response, setter_service=None):
        self.__request = request
        self.__repository = repository
        self.__response = response
        self.__setter_service = setter_service or UserSetterService(self.__repository)

    def __call__(self, user_id):
        try:
            fields = self.__request.get_data()
            self.__setter_service(user_id=user_id, **fields)
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
            log.exception(f"Error in UserSetterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",

            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
