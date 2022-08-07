from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.students.services.phone import PhoneGetterService
from tutorias_itsvc.students.services.phone import PhoneUpdaterService

log = get_logger(__file__)


class PhoneUpdaterController:
    def __init__(self, request, repository, response, service=None):
        self.__request = request
        self.__repository = repository
        self.__response = response
        self.__service = service or PhoneUpdaterService(self.__repository)

    def get_phone(self, student_id, phone_id):
        phone_getter_service = PhoneGetterService(self.__repository)
        phone = phone_getter_service(student_id=student_id, id=phone_id)
        return phone

    def __call__(self, student_id, phone_id):
        try:
            fields = self.__request.get_data()
            phone = self.get_phone(student_id, phone_id)
            if not phone:
                raise Exception("Phone not found")
            self.__service(id=phone_id, **fields)
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
            log.exception(f"Error in PhoneUpdaterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
