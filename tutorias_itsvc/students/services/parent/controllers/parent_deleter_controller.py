from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.repositories import ParentRepository
from tutorias_itsvc.students.services.parent import ParentDeleterService

log = get_logger(__file__)


class ParentDeleterController:
    def __init__(self, response, parent_repository=None, getter_service=None):
        self.__response = response
        self.__parent_repository = parent_repository or ParentRepository()
        self.__service = getter_service or ParentDeleterService(parent_repository=self.__parent_repository)

    def __call__(self, student_id, type):
        try:
            self.__service(student_id=student_id, type=type)
            response_data = dict(
                    success=True,
                    message="All Ok",
                    data={},
                )
            http_status = status.HTTP_200_OK
            return self.__response(response_data, http_status=http_status)
        except Exception as err:
            log.exception(f"Error in ParentDeleterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
