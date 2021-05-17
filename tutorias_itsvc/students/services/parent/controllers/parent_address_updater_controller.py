from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.common.services.address import AddressUpdaterService
from tutorias_itsvc.common.services.address import AddressGetterService
from tutorias_itsvc.students.repositories import ParentRepository
from tutorias_itsvc.students.services.parent import ParentGetterService

log = get_logger(__file__)


class ParentAddressUpdaterController:
    def __init__(self, request, repository, response, service=None):
        self.__request = request
        self.__repository = repository
        self.__response = response
        self.__service = service or AddressUpdaterService(self.__repository)

    def get_parent(self, student_id, type):
        repository = ParentRepository()
        getter_service = ParentGetterService(repository)
        parent = getter_service(student_id=student_id, type=type)
        if not parent:
            raise Exception("No existe el padre")
        return parent

    def get_address(self, address_id):
        getter_service = AddressGetterService(self.__repository)
        address = getter_service(id=address_id)
        return address

    def __call__(self, student_id, type):
        try:
            parent = self.get_parent(student_id, type)
            if not parent:
                raise Exception('No existe el padre')
            if not parent.address_id:
                raise Exception('No existe registro de direccion')
            address = self.get_address(parent.address_id)
            fields = self.__request.get_data()
            self.__service(address.id, **fields)
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
            log.exception(f"Error in ParentCreatorController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
