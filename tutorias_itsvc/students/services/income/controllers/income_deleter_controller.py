from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.services.income import IncomeDeleterService
from tutorias_itsvc.students.repositories import StudentIncomeRepository

log = get_logger(__file__)


class IncomeDeleterController:
    def __init__(self, response, student_income_repository=None, deleter_service=None):
        self.__response = response
        self.__student_income_repository = student_income_repository or StudentIncomeRepository()
        self.__service = deleter_service or IncomeDeleterService(
            student_income_repository=self.__student_income_repository)

    def __call__(self, student_id):
        try:
            self.__service(student_id=student_id)
            response_data = dict(
                success=True,
                message="All Ok",
                data={},
            )
            http_status = status.HTTP_200_OK
            return self.__response(response_data, http_status=http_status)
        except Exception as err:
            log.exception(f"Error in IncomeDeleterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
