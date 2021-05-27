from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.users.repositories import SiblingRepository
from tutorias_itsvc.users.services.siblings import SiblingGetterService
from tutorias_itsvc.students.services.siblings import StudentSiblingGetterService

log = get_logger(__file__)


class SiblingGetterController:
    def __init__(self, repository, serializer, response, getter_service=None):
        self.__repository = repository
        self.__serializer = serializer
        self.__response = response
        self.__service = getter_service or StudentSiblingGetterService(self.__repository)

    def get_sibling(self, sibling_id):
        repository = SiblingRepository()
        creator_service = SiblingGetterService(repository)
        sibling = creator_service(id=sibling_id)
        return sibling

    def __call__(self, student_id, sibling_id):
        try:
            filters = dict(student_id=student_id, sibling_id=sibling_id)
            student_sibling = self.__service(**filters)
            if student_sibling:
                sibling = self.get_sibling(student_sibling.sibling_id)
                serializer_data = self.__serializer(sibling)
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
            log.exception(f"Error in SiblingGetterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
