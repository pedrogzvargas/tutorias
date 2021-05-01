from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.academy.services.period_number import PeriodNumberFilterService

log = get_logger(__file__)


class PeriodNumberFilterController:
    def __init__(self, repository, serializer, response, getter_service=None):
        self.__repository = repository
        self.__serializer = serializer
        self.__response = response
        self.__service = getter_service or PeriodNumberFilterService(self.__repository)

    def __call__(self, **kwargs):
        try:
            periods = self.__service(**kwargs)
            if periods:
                periods = periods.order_by('id')
                serializer_data = self.__serializer(periods)
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
            log.exception(f"Error in PeriodNumberFilterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
