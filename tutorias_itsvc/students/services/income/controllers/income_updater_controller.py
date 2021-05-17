from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.students.services.income import IncomeGetterService
from tutorias_itsvc.students.services.income import IncomeUpdaterService

log = get_logger(__file__)


class IncomeUpdaterController:
    def __init__(self, request, repository, response, service=None):
        self.__request = request
        self.__repository = repository
        self.__response = response
        self.__service = service or IncomeUpdaterService(self.__repository)

    def get_income(self, student_id):
        getter_service = IncomeGetterService(self.__repository)
        income = getter_service(student_id=student_id)
        return income

    def __call__(self, student_id):
        try:
            fields = self.__request.get_data()
            income = self.get_income(student_id)
            if not income:
                raise Exception("Income not found")
            self.__service(id=income.id, **fields)
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
            log.exception(f"Error in IncomeUpdaterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
