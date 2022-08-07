from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.repositories import AddressRepository
from tutorias_itsvc.students.repositories import StudentRepository
from shared.exceptions import SerializerApiException
from tutorias_itsvc.students.services.address import AddressCreatorService

log = get_logger(__file__)


class AddressCreatorController:
    def __init__(self, request, response, address_repository=None, student_repository=None, service=None):
        self.__request = request
        self.__response = response
        self.__address_repository = address_repository or AddressRepository()
        self.__student_repository = student_repository or StudentRepository()
        self.__service = service or AddressCreatorService(address_repository=self.__address_repository,
                                                          student_repository=self.__student_repository)

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
            log.exception(f"Error in AddressCreatorController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
