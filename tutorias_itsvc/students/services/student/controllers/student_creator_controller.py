from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.students.services.student import StudentCreatorService
from tutorias_itsvc.users.repositories import UserRepository
from tutorias_itsvc.users.services.user import UserCreatorService
from tutorias_itsvc.users.services.user import UserGetterService
from tutorias_itsvc.users.repositories import GroupRepository
from tutorias_itsvc.users.services.group import GroupGetterService
from django.contrib.auth.hashers import make_password

log = get_logger(__file__)


class StudentCreatorController:
    def __init__(self, request, repository, response, service=None):
        self.__request = request
        self.__repository = repository
        self.__response = response
        self.__service = service or StudentCreatorService(self.__repository)

    def get_user(self, username):
        repository = UserRepository()
        getter_service = UserGetterService(repository)
        user = getter_service(username=username)
        return user

    def create_user(self, username, password, first_name, last_name, second_name=None, second_last_name=None, email=None):
        repository = UserRepository()
        creator_service = UserCreatorService(repository)
        user = creator_service(
            username=username,
            password=password,
            first_name=first_name,
            last_name=last_name,
            second_name=second_name,
            second_last_name=second_last_name,
            email=email)
        return user

    def get_group(self, group_name):
        repository = GroupRepository()
        getter_service = GroupGetterService(repository)
        group = getter_service(name=group_name)
        return group

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
                email=fields.get('email')
            )
            student_group = self.get_group('student')
            if not student_group:
                raise Exception("No existe un grupo")
            user.groups.add(student_group)
            self.__service(user_id=user.id, enrollment=fields.get('username'))
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
            log.exception(f"Error in StudentCreatorController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
