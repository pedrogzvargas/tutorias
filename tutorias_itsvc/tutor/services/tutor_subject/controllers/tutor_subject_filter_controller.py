from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.tutor.services.tutor_subject import TutorSubjectFilterService
from rest_framework.generics import GenericAPIView
from rest_framework import filters

log = get_logger(__file__)


class TutorSubjectFilterController(GenericAPIView):
    search_fields = [
        'tutor__user__first_name',
        'tutor__user__last_name',
        'subject__name',
        'subject__code',
        'school_cycle__name'
    ]
    filter_backends = (filters.SearchFilter,)

    def __init__(self, repository, serializer, request, response, service=None):
        self.request = request
        self.__repository = repository
        self.__serializer = serializer
        self.__response = response
        self.__service = service or TutorSubjectFilterService(self.__repository)

    def __call__(self, **kwargs):
        try:
            tutor_subject = self.__service(**kwargs)
            tutor_subject = self.filter_queryset(tutor_subject)
            if tutor_subject:
                page = self.paginate_queryset(tutor_subject)
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
            log.exception(f"Error in TutorSubjectGetterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
