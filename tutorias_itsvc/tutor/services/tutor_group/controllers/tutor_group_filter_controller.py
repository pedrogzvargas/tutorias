from rest_framework import status
from rest_framework import filters
from shared.utils import get_logger
from rest_framework.generics import GenericAPIView
from tutorias_itsvc.tutor.services.tutor_group import TutorGroupFilterService

log = get_logger(__file__)


class TutorGroupFilterController(GenericAPIView):
    search_fields = [
        'tutor__user__first_name',
        'tutor__user__last_name',
        'academic_group__academic_period_number__academic_period__academic_major__major__name',
        'academic_group__academic_period_number__period_number__name',
        'school_cycle__name'
    ]
    filter_backends = (filters.SearchFilter,)

    def __init__(self, repository, serializer, request, response, service=None):
        self.request = request
        self.__repository = repository
        self.__serializer = serializer
        self.__response = response
        self.__service = service or TutorGroupFilterService(self.__repository)

    def __call__(self, **kwargs):
        try:
            tutor_group = self.__service(**kwargs)
            tutor_group = self.filter_queryset(tutor_group)
            if tutor_group:
                page = self.paginate_queryset(tutor_group)
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
            log.exception(f"Error in TutorGroupFilterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
