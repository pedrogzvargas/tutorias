from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.students.services.income import IncomeCreatorService
from tutorias_itsvc.students.repositories import StudentIncomeRepository
from tutorias_itsvc.students.repositories import StudentRepository

log = get_logger(__file__)


class IncomeCreatorController:
    def __init__(self, request, response, student_income_repository=None, student_repository=None, service=None):
        self.__request = request
        self.__response = response
        self.__student_income_repository = student_income_repository or StudentIncomeRepository()
        self.__student_repository = student_repository or StudentRepository()
        self.__service = service or IncomeCreatorService(
            student_income_repository=self.__student_income_repository,
            student_repository=self.__student_repository
        )

    def __call__(self, student_id):
        try:
            fields = self.__request.get_data()
            self.__service(student_id=student_id, **fields)
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
            log.exception(f"Error in IncomeCreatorController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
