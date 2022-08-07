from django.db import transaction
from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.users.repositories import UserRepository
from tutorias_itsvc.users.repositories import GroupRepository
from tutorias_itsvc.students.services.student import StudentCreatorService

log = get_logger(__file__)


class StudentCreatorController:
    def __init__(self,
                 request,
                 response,
                 student_repository=None,
                 user_repository=None,
                 group_repository=None,
                 service=None):
        self.__request = request
        self.__response = response
        self.__student_repository = student_repository or StudentRepository()
        self.__user_repository = user_repository or UserRepository()
        self.__group_repository = group_repository or GroupRepository()
        self.__service = service or StudentCreatorService(student_repository=self.__student_repository,
                                                          user_repository=self.__user_repository,
                                                          group_repository=self.__group_repository)

    @transaction.atomic
    def __call__(self):
        try:
            fields = self.__request.get_data()
            self.__service(**fields)
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
