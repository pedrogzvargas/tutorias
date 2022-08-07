from rest_framework import status
from rest_framework import filters
from shared.utils import get_logger
from rest_framework.generics import GenericAPIView
from tutorias_itsvc.students.services.academic_information import AcademicInformationFilterService

log = get_logger(__file__)


class StudentAcademicInformationFilterController(GenericAPIView):
    search_fields = [
        'student__user__first_name',
        'student__user__last_name',
    ]
    filter_backends = (filters.SearchFilter,)

    def __init__(self, repository, serializer, request, response, service=None):
        self.request = request
        self.__repository = repository
        self.__serializer = serializer
        self.__response = response
        self.__service = service or AcademicInformationFilterService(self.__repository)

    def __call__(self, **kwargs):
        try:
            student = self.__service(**kwargs)
            student = self.filter_queryset(student)
            if student:
                page = self.paginate_queryset(student)
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
            log.exception(f"Error in StudentAcademicInformationFilterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
