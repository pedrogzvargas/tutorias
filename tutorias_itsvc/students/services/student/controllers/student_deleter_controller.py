from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.users.repositories import UserRepository
from tutorias_itsvc.students.services.student import StudentDeleterService

log = get_logger(__file__)


class StudentDeleterController:
    def __init__(self, response, student_repository=None, user_repository=None, service=None):
        self.__response = response
        self.__student_repository = student_repository or StudentRepository()
        self.__user_repository = user_repository or UserRepository()
        self.__service = service or StudentDeleterService(student_repository=self.__student_repository,
                                                          user_repository=self.__user_repository)

    def __call__(self, student_id):
        try:
            self.__service(student_id=student_id)
            response_data = dict(
                    success=True,
                    message="All Ok",
                )
            http_status = status.HTTP_200_OK
            return self.__response(response_data, http_status=http_status)
        except Exception as err:
            log.exception(f"Error in StudentDeleterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
