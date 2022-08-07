from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.courses.repositories import StudetCourseRepository
from tutorias_itsvc.courses.services.student_course import StudetCourseGetterService
from tutorias_itsvc.courses.serializers.api.v1.course import StudetCourseSerializer

log = get_logger(__file__)


class StudentCourseGetterController:
    def __init__(self, response, serializer=None, student_course_repository=None, service=None):
        self.__response = response
        self.__serializer = serializer or StudetCourseSerializer()
        self.__student_course_repository = student_course_repository or StudetCourseRepository()
        self.__service = service or StudetCourseGetterService(repository=self.__student_course_repository)

    def __call__(self, **kwargs):
        try:
            course = self.__service(**kwargs)
            if course:
                serializer_data = self.__serializer(course)
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
            log.exception(f"Error in StudentCourseGetterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
