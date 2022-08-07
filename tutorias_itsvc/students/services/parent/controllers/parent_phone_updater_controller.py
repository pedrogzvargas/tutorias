from rest_framework import status
from shared.utils import get_logger

from tutorias_itsvc.users.services.person_phone import PersonPhoneGetterService
from tutorias_itsvc.users.services.person_phone import PersonPhoneUpdaterService

from tutorias_itsvc.students.repositories import ParentRepository
from tutorias_itsvc.students.services.parent import ParentGetterService

log = get_logger(__file__)


class ParentPhoneUpdaterController:
    def __init__(self, request, repository, response, service=None):
        self.__request = request
        self.__repository = repository
        self.__response = response
        self.__service = service or PersonPhoneUpdaterService(self.__repository)

    def get_parent(self, student_id, type):
        repository = ParentRepository()
        getter_service = ParentGetterService(repository)
        parent = getter_service(student_id=student_id, type=type)
        if not parent:
            raise Exception("No existe el padre")
        return parent

    def get_phone(self, person_id, phone_id):
        getter_service = PersonPhoneGetterService(self.__repository)
        phone = getter_service(person_id=person_id, id=phone_id)
        return phone

    def __call__(self, student_id, type, phone_id):
        try:
            parent = self.get_parent(student_id, type)
            if not parent:
                raise Exception("No existe un padre registrado")
            phone = self.get_phone(phone_id=phone_id, person_id=parent.id)
            fields = self.__request.get_data()
            if phone:
                self.__service(id=phone.id, **fields)
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
            log.exception(f"Error in ParentPhoneUpdaterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
