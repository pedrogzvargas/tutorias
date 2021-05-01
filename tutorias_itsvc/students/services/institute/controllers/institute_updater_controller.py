from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.students.services.institute import InstituteUpdaterService, InstituteGetterService

log = get_logger(__file__)


class InstituteUpdaterController:
    def __init__(self, request, repository, response, service=None):
        self.__request = request
        self.__repository = repository
        self.__response = response
        self.__service = service or InstituteUpdaterService(self.__repository)

    def __call__(self, student_id, institute_id):
        try:
            fields = self.__request.get_data()
            institute_getter_service = InstituteGetterService(self.__repository)
            institute = institute_getter_service(student_id=student_id, id=institute_id)
            if not institute:
                raise Exception("Institute not found")
            self.__service(id=institute_id, **fields)
            response_data = dict(
                success=True,
                message="All Ok",
                data={},
            )
            return self.__response(response_data, http_status=status.HTTP_200_OK)
        except SerializerApiException as err:
            response_data = dict(
                success=False,
                message=f"{err}",
                errors=err.errors
            )
            return self.__response(response_data, http_status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            log.exception(f"Error in InstituteUpdaterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
