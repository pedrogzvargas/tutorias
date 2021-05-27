from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.repositories import StudentSiblingRepository
from tutorias_itsvc.users.services.siblings import SiblingUpdaterService
from tutorias_itsvc.students.services.siblings import StudentSiblingGetterService

log = get_logger(__file__)


class SiblingUpdaterController:
    def __init__(self, request, repository, response, service=None):
        self.__request = request
        self.__repository = repository
        self.__response = response
        self.__service = service or SiblingUpdaterService(self.__repository)

    def get_sibling(self, student_id, sibling_id):
        repository = StudentSiblingRepository()
        getter_service = StudentSiblingGetterService(repository)
        sibling = getter_service(student_id=student_id, sibling_id=sibling_id)
        return sibling

    def __call__(self, student_id, sibling_id):
        try:
            fields = self.__request.get_data()
            student_sibling = self.get_sibling(student_id, sibling_id)
            if student_sibling:
                self.__service(student_sibling.sibling_id, **fields)
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
            log.exception(f"Error in SiblingUpdaterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
