from rest_framework import status

from shared.utils import get_logger
from shared.exceptions import SerializerApiException

from tutorias_itsvc.users.services.person_phone import PersonPhoneCreatorService

from tutorias_itsvc.students.repositories import ParentRepository
from tutorias_itsvc.students.services.parent import ParentGetterService

log = get_logger(__file__)


class ParentPhoneCreatorController:
    def __init__(self, request, repository, response, service=None):
        self.__request = request
        self.__repository = repository
        self.__response = response
        self.__service = service or PersonPhoneCreatorService(self.__repository)

    def get_parent(self, student_id, type):
        repository = ParentRepository()
        getter_service = ParentGetterService(repository)
        parent = getter_service(student_id=student_id, type=type)
        return parent

    def __call__(self, student_id, type):
        try:
            parent = self.get_parent(student_id, type)
            if not parent:
                raise Exception("No existe el padre")
            fields = self.__request.get_data()
            fields.update(dict(person_id=parent.id))
            self.__service(**fields)
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
            log.exception(f"Error in ParentPhoneCreatorController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
