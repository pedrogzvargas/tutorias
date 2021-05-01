from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.users.services.auth import DjangoLogin
from tutorias_itsvc.users.services.role import RoleGetterService
from tutorias_itsvc.users.utils import FullNameGetter
from tutorias_itsvc.users.services.profile_image import ProfileImageFilterService
from tutorias_itsvc.users.repositories import ProfileImageRepository

log = get_logger(__file__)


class LoginController:
    def __init__(self, request, serializer, response, service=DjangoLogin):
        self.__request = request
        self.__serializer = serializer
        self.__response = response
        self.__service = service

    def get_full_name(self, user):
        full_name_getter = FullNameGetter(user)
        full_name = full_name_getter()
        return full_name

    def get_user_roles(self, user):
        role_getter_service = RoleGetterService(user=user)
        roles = role_getter_service()
        return roles

    def get_profile_image(self, user):
        profile_image_url = None
        repository = ProfileImageRepository()
        profile_image_filter_service = ProfileImageFilterService(repository)
        profile_image = profile_image_filter_service(user=user).last()
        if profile_image:
            profile_image_url = profile_image.profile_image
        return profile_image_url

    def __call__(self):
        try:
            fields = self.__request.get_data()
            login_service = self.__service(**fields)
            auth_information = login_service()
            roles = self.get_user_roles(user=auth_information.user)
            fullname = self.get_full_name(user=auth_information.user)
            profile_image = self.get_profile_image(user=auth_information.user)
            auth_information.roles = roles
            auth_information.fullname = fullname
            auth_information.profile_image = profile_image
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
