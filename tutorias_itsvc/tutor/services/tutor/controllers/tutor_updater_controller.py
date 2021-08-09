from django.contrib.auth.hashers import make_password
from django.db import transaction
from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.tutor.services.tutor import TutorUpdaterService
from tutorias_itsvc.users.services.user import UserGetterService, UserUpdaterService

log = get_logger(__file__)


class TutorUpdaterController:
    def __init__(self, request, tutor_repository, user_repository, response, service=None):
        self.__request = request
        self.__tutor_repository = tutor_repository
        self.__user_repository = user_repository
        self.__response = response
        self.__service = service or TutorUpdaterService(self.__tutor_repository)

    def get_user(self, username):
        getter_service = UserGetterService(self.__user_repository)
        user = getter_service(username=username)
        return user

    def update_user(self, id, username, first_name, last_name, second_name=None, second_last_name=None, password=None):
        updater_service = UserUpdaterService(self.__user_repository)
        updater_parameters = dict(
            id=id,
            username=username,
            first_name=first_name,
            last_name=last_name,
            second_name=second_name,
            second_last_name=second_last_name
        )
        if password:
            updater_parameters.update(dict(password=password))
        user = updater_service(**updater_parameters)
        return user

    @transaction.atomic
    def __call__(self, tutor_id):
        try:
            fields = self.__request.get_data()
            tutor = self.__tutor_repository.get(id=tutor_id)
            if not tutor:
                raise Exception("No existe el tutor")
            user = tutor.user
            self.update_user(
                id=user.id,
                username=fields.get('username'),
                password=make_password(fields.get('password')),
                first_name=fields.get('first_name'),
                last_name=fields.get('last_name'),
                second_name=fields.get('second_name'),
                second_last_name=fields.get('second_last_name'),
            )
            self.__service(
                id=tutor_id,
                user_id=user.id,
                enrollment=fields.get('username'),
                academic_id=fields.get("academic_id"),
                is_active=fields.get("is_active", True)
            )
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
            log.exception(f"Error in TutorUpdaterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
