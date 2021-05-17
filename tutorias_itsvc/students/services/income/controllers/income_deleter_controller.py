from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.services.income import IncomeGetterService
from tutorias_itsvc.students.services.institute import InstituteDeleterService

log = get_logger(__file__)


class IncomeDeleterController:
    def __init__(self, repository, response, deleter_service=None):
        self.__repository = repository
        self.__response = response
        self.__service = deleter_service or InstituteDeleterService(self.__repository)

    def get_income(self, student_id):
        getter_service = IncomeGetterService(self.__repository)
        income = getter_service(student_id=student_id)
        return income

    def __call__(self, student_id):
        try:
            income = self.get_income(student_id)
            if income:
                self.__service(id=income.id)
                response_data = dict(
                    success=True,
                    message="All Ok",
                    data={},
                )
                http_status = status.HTTP_200_OK
            else:
                response_data = dict(
                    success=False,
                    message="Not Found",
                    data={},
                )
                http_status = status.HTTP_404_NOT_FOUND
            return self.__response(response_data, http_status=http_status)
        except Exception as err:
            log.exception(f"Error in IncomeDeleterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
