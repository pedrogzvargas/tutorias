from rest_framework import status
from rest_framework import filters
from shared.utils import get_logger
from rest_framework.generics import GenericAPIView
from tutorias_itsvc.tutor.services.tutor import TutorFilterService

log = get_logger(__file__)


class TutorFilterController(GenericAPIView):
    search_fields = [
        'user__first_name',
        'user__last_name',
        'enrollment',
    ]
    filter_backends = (filters.SearchFilter,)

    def __init__(self, repository, serializer, request, response, service=None):
        self.request = request
        self.__repository = repository
        self.__serializer = serializer
        self.__response = response
        self.__service = service or TutorFilterService(self.__repository)

    def __call__(self, **kwargs):
        try:
            tutor = self.__service(**kwargs)
            tutor = self.filter_queryset(tutor)
            if tutor:
                get_all = self.request.query_params.get('get_all', False)
                if get_all:
                    serializer_data = self.__serializer(tutor)
                    return self.__response(serializer_data, http_status=status.HTTP_200_OK)

                page = self.paginate_queryset(tutor)
                if page:
                    serializer_data = self.__serializer(page)
                    return self.get_paginated_response(serializer_data)
            else:
                response_data = dict(
                    success=False,
                    message="Not Found",
                    data={},
                )
                http_status = status.HTTP_404_NOT_FOUND
                return self.__response(response_data, http_status=http_status)
        except Exception as err:
            log.exception(f"Error in TutorFilterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
