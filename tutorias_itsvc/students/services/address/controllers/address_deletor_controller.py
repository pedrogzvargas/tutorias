from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.repositories import AddressRepository
from tutorias_itsvc.students.services.address import AddressGetterService
from tutorias_itsvc.students.services.address import AddressDeleterService

log = get_logger(__file__)


class AddressDeleterController:
    def __init__(self, repository, response, deleter_service=None):
        self.__repository = repository
        self.__response = response
        self.__service = deleter_service or AddressDeleterService(self.__repository)

    def get_address(self, student_id):
        repository = AddressRepository()
        getter_service = AddressGetterService(repository=repository)
        address = getter_service(student_id=student_id)
        return address

    def __call__(self, student_id):
        try:
            address = self.get_address(student_id)
            if address:
                self.__service(id=address.id)
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
            log.exception(f"Error in AddressDeleterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
