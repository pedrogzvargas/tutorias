from django.contrib.auth.hashers import make_password
from django.db import transaction
from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.tutor.services.tutor import TutorCreatorService
from tutorias_itsvc.users.services.group import GroupGetterService
from tutorias_itsvc.users.services.user import UserCreatorService, UserGetterService

log = get_logger(__file__)


class TutorCreatorController:
    def __init__(self, request, tutor_repository, user_repository, group_repository, response, service=None):
        self.__request = request
        self.__tutor_repository = tutor_repository
        self.__user_repository = user_repository
        self.__group_repository = group_repository
        self.__response = response
        self.__service = service or TutorCreatorService(self.__tutor_repository)

    def get_user(self, username):
        getter_service = UserGetterService(self.__user_repository)
        user = getter_service(username=username)
        return user

    def get_group(self, group_name):
        getter_service = GroupGetterService(self.__group_repository)
        group = getter_service(name=group_name)
        return group

    def create_user(self, username, password, first_name, last_name, second_name=None, second_last_name=None):
        creator_service = UserCreatorService(self.__user_repository)
        user = creator_service(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            second_name=second_name,
            second_last_name=second_last_name)
        return user

    @transaction.atomic
    def __call__(self):
        try:
            fields = self.__request.get_data()
            user = self.get_user(fields.get('username'))
            if user:
                raise Exception('Ya existe un usuario con este nombre de usuario')
            user = self.create_user(
                username=fields.get('username'),
                password=make_password(fields.get('password')),
                first_name=fields.get('first_name'),
                last_name=fields.get('last_name'),
                second_name=fields.get('second_name'),
                second_last_name=fields.get('second_last_name'),
            )
            tutor_group = self.get_group('tutor')
            if not tutor_group:
                raise Exception("No existe el grupo que deseas asignar")
            user.groups.add(tutor_group)
            self.__service(
                user=user,
                enrollment=fields.get('username'),
                academic_id=fields.get("academic_id"),
                is_active=fields.get("is_active", True)
            )
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
            log.exception(f"Error in TutorCreatorController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
