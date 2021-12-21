from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.services.interview import InterviewGetterService

log = get_logger(__file__)


class InterviewGetterController:
    def __init__(self, request, repository, serializer, response, getter_service=None):
        self.__request = request
        self.__repository = repository
        self.__serializer = serializer
        self.__response = response
        self.__service = getter_service or InterviewGetterService(request=self.__request, repository=self.__repository)

    def __call__(self, **kwargs):
        try:
            interview = self.__service(**kwargs)
            if interview:
                serializer_data = self.__serializer(interview)
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
            log.exception(f"Error in InterviewGetterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
