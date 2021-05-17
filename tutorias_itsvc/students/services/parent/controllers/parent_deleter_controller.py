from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.services.parent import ParentGetterService
from tutorias_itsvc.students.services.parent import ParentDeleterService

log = get_logger(__file__)


class ParentDeleterController:
    def __init__(self, repository, response, getter_service=None):
        self.__repository = repository
        self.__response = response
        self.__service = getter_service or ParentDeleterService(self.__repository)

    def get_parent(self, student_id, type):
        getter_service = ParentGetterService(self.__repository)
        parent = getter_service(student_id=student_id, type=type)
        return parent

    def __call__(self, student_id, type):
        try:
            parent = self.get_parent(student_id, type)
            if parent:
                self.__service(id=parent.id)
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
            log.exception(f"Error in ParentDeleterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
