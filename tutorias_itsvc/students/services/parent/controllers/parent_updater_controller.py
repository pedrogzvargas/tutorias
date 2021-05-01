from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.students.services.parent import ParentGetterService
from tutorias_itsvc.students.services.parent import ParentUpdaterService

log = get_logger(__file__)


class ParentUpdaterController:
    def __init__(self, request, repository, response, service=None):
        self.__request = request
        self.__repository = repository
        self.__response = response
        self.__service = service or ParentUpdaterService(self.__repository)

    def __call__(self, student_id, type):
        try:
            getter_service = ParentGetterService(self.__repository)
            parent = getter_service(student_id=student_id, type=type)
            if not parent:
                raise Exception("Parent dont exist")
            fields = self.__request.get_data()
            fields.update(dict(student_id=student_id, type=type))
            self.__service(id=parent.id, **fields)
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
            log.exception(f"Error in ParentUpdaterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
