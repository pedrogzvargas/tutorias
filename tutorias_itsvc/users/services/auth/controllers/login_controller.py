from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.users.services.auth import DjangoLogin
from tutorias_itsvc.users.services.role import RoleGetterService

log = get_logger(__file__)


class LoginController:
    def __init__(self, request, serializer, response, service=DjangoLogin):
        self.__request = request
        self.__serializer = serializer
        self.__response = response
        self.__service = service

    def __call__(self):
        try:
            fields = self.__request.get_data()
            login_service = self.__service(**fields)
            auth_information = login_service()
            role_getter_service = RoleGetterService(user=auth_information.user)
            roles = role_getter_service()
            auth_information.roles = roles
            serializer_data = self.__serializer(auth_information)
            response_data = dict(
                success=True,
                message="All Ok",
                data=serializer_data,
            )
            return self.__response(response_data, http_status=status.HTTP_200_OK)
        except ValueError as err:
            log.exception(f"Error in LoginController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",

            )
            return self.__response(response_data, http_status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            log.exception(f"Error in LoginController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",

            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
