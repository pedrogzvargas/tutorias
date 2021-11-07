from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.students.services.parent import ParentCreatorService
from tutorias_itsvc.students.repositories import ParentRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.common.repositories import AcademicDegreeRepository

log = get_logger(__file__)


class ParentCreatorController:
    def __init__(self,
                 request,
                 response,
                 parent_repository=None,
                 student_repository=None,
                 academic_degree_repository=None,
                 service=None):
        self.__request = request
        self.__response = response
        self.__parent_repository = parent_repository or ParentRepository()
        self.__student_repository = student_repository or StudentRepository()
        self.__academic_degree_repository = academic_degree_repository or AcademicDegreeRepository()
        self.__service = service or ParentCreatorService(parent_repository=self.__parent_repository,
                                                         student_repository=self.__student_repository,
                                                         academic_degree_repository=self.__academic_degree_repository)

    def __call__(self, student_id, type):
        try:
            fields = self.__request.get_data()
            self.__service(student_id=student_id, type=type, **fields)
            response_data = dict(
                success=True,
                message="All Ok",
                data={},
            )
            return self.__response(response_data, http_status=status.HTTP_201_CREATED)
        except SerializerApiException as err:
            response_data = dict(
                success=False,
                message=f"{err}",
                errors=err.errors
            )
            return self.__response(response_data, http_status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            log.exception(f"Error in ParentCreatorController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
