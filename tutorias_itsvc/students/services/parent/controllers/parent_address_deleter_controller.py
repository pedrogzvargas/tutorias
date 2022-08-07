from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.services.parent import ParentAddressDeleterService
from tutorias_itsvc.students.repositories import ParentRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.common.repositories import AddressRepository

log = get_logger(__file__)


class ParentAddressDeleterController:
    def __init__(self,
                 response,
                 parent_repository=None,
                 student_repository=None,
                 address_repository=None,
                 service=None):
        self.__response = response
        self.__parent_repository = parent_repository or ParentRepository()
        self.__student_repository = student_repository or StudentRepository()
        self.__address_repository = address_repository or AddressRepository()
        self.__service = service or ParentAddressDeleterService(parent_repository=self.__parent_repository,
                                                                student_repository=self.__student_repository,
                                                                address_repository=self.__address_repository)

    def __call__(self, student_id, type):
        try:
            self.__service(student_id=student_id, type=type)
            response_data = dict(
                success=True,
                message="All Ok",
                data={},
            )
            http_status = status.HTTP_200_OK
            return self.__response(response_data, http_status=http_status)
        except Exception as err:
            log.exception(f"Error in ParentGetterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
