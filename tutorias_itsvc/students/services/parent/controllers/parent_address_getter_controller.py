from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.repositories import ParentRepository
from tutorias_itsvc.students.services.parent import ParentGetterService
from tutorias_itsvc.common.services.address import AddressGetterService

log = get_logger(__file__)


class ParentAddressGetterController:
    def __init__(self, repository, serializer, response, getter_service=None):
        self.__repository = repository
        self.__serializer = serializer
        self.__response = response
        self.__service = getter_service or AddressGetterService(self.__repository)

    def get_parent(self, student_id, type):
        repository = ParentRepository()
        getter_service = ParentGetterService(repository)
        parent = getter_service(student_id=student_id, type=type)
        if not parent:
            raise Exception("No existe el padre")
        return parent

    def __call__(self, student_id, type):
        try:
            parent = self.get_parent(student_id, type)
            if not parent:
                raise Exception("No existe un padre registrado")
            address = self.__service(id=parent.address_id)
            if address:
                serializer_data = self.__serializer(address)
                response_data = dict(
                    success=True,
                    message="All Ok",
                    data=serializer_data,
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
            log.exception(f"Error in ParentGetterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
