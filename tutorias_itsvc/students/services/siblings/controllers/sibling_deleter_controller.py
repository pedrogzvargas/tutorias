from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.users.repositories import SiblingRepository
from tutorias_itsvc.users.services.siblings import SiblingDeleterService
from tutorias_itsvc.students.services.siblings import StudentSiblingGetterService
from tutorias_itsvc.students.services.siblings import StudentSiblingDeleterService

log = get_logger(__file__)


class SiblingDeleterController:
    def __init__(self, repository, response, service=None):
        self.__repository = repository
        self.__response = response
        self.__service = service or StudentSiblingDeleterService(self.__repository)

    def get_student_sibling(self, student_id, sibling_id):
        getter_service = StudentSiblingGetterService(self.__repository)
        student_sibling = getter_service(student_id=student_id, sibling_id=sibling_id)
        return student_sibling

    def delete_sibling(self, sibling_id):
        repository = SiblingRepository()
        deleter_service = SiblingDeleterService(repository)
        deleter_service(id=sibling_id)

    def __call__(self, student_id, sibling_id):
        try:
            student_sibling = self.get_student_sibling(student_id, sibling_id)
            if student_sibling:
                self.__service(id=student_sibling.id)
                self.delete_sibling(student_sibling.sibling_id)
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
            log.exception(f"Error in SiblingGetterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
