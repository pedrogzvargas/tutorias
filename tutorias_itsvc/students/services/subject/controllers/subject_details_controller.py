from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.services.subject import SubjectDetailsService

log = get_logger(__file__)


class SubjectDetailsController:
    def __init__(self, serializer, response):
        self.__serializer = serializer
        self.__response = response
        # self.__service = service

    def __call__(self, student_id):
        try:
            service = SubjectDetailsService(student_id)
            subject = service()
            if subject:
                serializer_data = self.__serializer(subject)
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
            log.exception(f"Error in SubjectDetailsController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
