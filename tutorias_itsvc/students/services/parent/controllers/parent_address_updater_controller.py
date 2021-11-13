from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.students.services.parent import ParentAddressUpdaterService
from tutorias_itsvc.students.repositories import ParentRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.common.repositories import AddressRepository
from tutorias_itsvc.common.repositories import StateRepository

log = get_logger(__file__)


class ParentAddressUpdaterController:
    def __init__(self,
                 request,
                 response,
                 parent_repository=None,
                 student_repository=None,
                 address_repository=None,
                 state_repository=None,
                 service=None):
        self.__request = request
        self.__response = response
        self.__parent_repository = parent_repository or ParentRepository()
        self.__student_repository = student_repository or StudentRepository()
        self.__address_repository = address_repository or AddressRepository()
        self.__state_repository = state_repository or StateRepository()
        self.__service = service or ParentAddressUpdaterService(parent_repository=self.__parent_repository,
                                                                student_repository=self.__student_repository,
                                                                address_repository=self.__address_repository,
                                                                state_repository=self.__state_repository)

    def __call__(self, student_id, type):
        try:
            fields = self.__request.get_data()
            self.__service(student_id=student_id, type=type, **fields)
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
            log.exception(f"Error in ParentCreatorController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
