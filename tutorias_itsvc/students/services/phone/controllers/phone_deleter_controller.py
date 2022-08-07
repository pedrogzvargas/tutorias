from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.services.phone import PhoneGetterService
from tutorias_itsvc.students.services.phone import PhoneDeleterService

log = get_logger(__file__)


class PhoneDeleterController:
    def __init__(self, repository, response, deleter_service=None):
        self.__repository = repository
        self.__response = response
        self.__service = deleter_service or PhoneDeleterService(self.__repository)

    def get_phone(self, student_id, phone_id):
        phone_getter_service = PhoneGetterService(self.__repository)
        phone = phone_getter_service(student_id=student_id, id=phone_id)
        return phone

    def __call__(self, student_id, phone_id):
        try:
            phone = self.get_phone(student_id, phone_id)
            if phone:
                self.__service(id=phone.id)
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
            log.exception(f"Error in PhoneDeleterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
