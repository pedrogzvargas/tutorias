from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.students.services.scholarship import StudentScholarshipGetterService
from tutorias_itsvc.students.repositories import StudentScholarshipRepository

log = get_logger(__file__)


class StudentScholarshipGetterController:
    def __init__(self,
                 response,
                 serializer,
                 student_scholarship_repository=None,
                 service=None):
        self.__response = response
        self.__serializer = serializer
        self.__student_scholarship_repository = student_scholarship_repository or StudentScholarshipRepository()
        self.__service = service or StudentScholarshipGetterService(repository=self.__student_scholarship_repository)

    def __call__(self, **kwargs):
        try:
            scholarship = self.__service(**kwargs)
            if scholarship:
                serializer_data = self.__serializer(scholarship)
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
        except SerializerApiException as err:
            response_data = dict(
                success=False,
                message=f"{err}",
                errors=err.errors
            )
            return self.__response(response_data, http_status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            log.exception(f"Error in StudentScholarshipGetterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
