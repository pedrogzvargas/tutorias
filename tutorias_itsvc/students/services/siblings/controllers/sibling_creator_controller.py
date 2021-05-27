from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.users.repositories import SiblingRepository
from tutorias_itsvc.users.services.siblings import SiblingCreatorService
from tutorias_itsvc.students.services.siblings import StudentSiblingCreatorService

log = get_logger(__file__)


class SiblingCreatorController:
    def __init__(self, request, repository, response, service=None):
        self.__request = request
        self.__repository = repository
        self.__response = response
        self.__service = service or StudentSiblingCreatorService(self.__repository)

    def create_sibling(self, payload):
        repository = SiblingRepository()
        creator_service = SiblingCreatorService(repository)
        sibling = creator_service(**payload)
        return sibling

    def __call__(self, student_id):
        try:
            fields = self.__request.get_data()
            sibling = self.create_sibling(fields)
            if not sibling:
                raise Exception('Error al crear el hermano')
            self.__service(student_id=student_id, sibling_id=sibling.id)
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
            log.exception(f"Error in SiblingCreatorController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
