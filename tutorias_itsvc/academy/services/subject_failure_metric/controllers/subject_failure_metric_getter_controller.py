from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.academy.services.subject_failure_metric import SubjectFailureMetricGetterService

log = get_logger(__file__)


class SubjectFailureMetricGetterController:
    def __init__(self, repository, serializer, response, service=None):
        self.__repository = repository
        self.__serializer = serializer
        self.__response = response
        self.__service = service or SubjectFailureMetricGetterService(self.__repository)

    def __call__(self, **kwargs):
        try:
            subject_failure_metric = self.__service(**kwargs)
            if subject_failure_metric:
                serializer_data = self.__serializer(subject_failure_metric)
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
            log.exception(f"Error in SubjectFailureMetricGetterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
