from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.users.repositories import SiblingRepository
from tutorias_itsvc.users.services.siblings import SiblingFilterService
from tutorias_itsvc.students.services.siblings import StudentSiblingFilterService

log = get_logger(__file__)


class SiblingFilterController:
    def __init__(self, repository, serializer, response, service=None):
        self.__repository = repository
        self.__serializer = serializer
        self.__response = response
        self.__service = service or StudentSiblingFilterService(self.__repository)

    def get_siblings(self, sibling_ids):
        repository = SiblingRepository()
        getter_service = SiblingFilterService(repository)
        sibling = getter_service(id__in=sibling_ids)
        return sibling

    def __call__(self, student_id):
        try:
            student_sibling = self.__service(student_id=student_id)
            if student_sibling:
                sibling_ids = student_sibling.values_list('sibling_id', flat=True)
                siblings = self.get_siblings(sibling_ids)
                serializer_data = self.__serializer(siblings)
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
