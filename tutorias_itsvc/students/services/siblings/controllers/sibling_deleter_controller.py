from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.services.siblings import StudentSiblingDeleterService
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.repositories import StudentSiblingRepository
from tutorias_itsvc.users.repositories import SiblingRepository

log = get_logger(__file__)


class SiblingDeleterController:
    def __init__(self,
                 response,
                 sibling_repository=None,
                 student_repository=None,
                 student_sibling_repository=None,
                 service=None):
        self.__response = response
        self.__sibling_repository = sibling_repository or SiblingRepository()
        self.__student_repository = student_repository or StudentRepository()
        self.__student_sibling_repository = student_sibling_repository or StudentSiblingRepository()
        self.__service = service or StudentSiblingDeleterService(
            sibling_repository=self.__sibling_repository,
            student_repository=self.__student_repository,
            student_sibling_repository=self.__student_sibling_repository,
        )

    def __call__(self, student_id, sibling_id):
        try:
            self.__service(student_id=student_id, sibling_id=sibling_id)
            response_data = dict(
                success=True,
                message="All Ok",
                data={},
            )
            http_status = status.HTTP_200_OK
            return self.__response(response_data, http_status=http_status)
        except Exception as err:
            log.exception(f"Error in SiblingGetterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
