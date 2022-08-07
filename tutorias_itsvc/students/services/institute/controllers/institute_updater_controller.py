from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.students.services.institute import InstituteUpdaterService
from tutorias_itsvc.students.repositories import StudentInstituteRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.common.repositories import AcademicDegreeRepository

log = get_logger(__file__)


class InstituteUpdaterController:
    def __init__(self,
                 request,
                 response,
                 student_institute_repository=None,
                 student_repository=None,
                 academic_degree_repository=None,
                 service=None):
        self.__request = request
        self.__response = response
        self.__student_institute_repository = student_institute_repository or StudentInstituteRepository()
        self.__student_repository = student_repository or StudentRepository()
        self.__academic_degree_repository = academic_degree_repository or AcademicDegreeRepository()
        self.__service = service or InstituteUpdaterService(
            student_institute_repository=self.__student_institute_repository,
            student_repository=self.__student_repository,
            academic_degree_repository=self.__academic_degree_repository)

    def __call__(self, student_id, institute_id):
        try:
            fields = self.__request.get_data()
            self.__service(institute_id=institute_id, student_id=student_id, **fields)
            response_data = dict(
                success=True,
                message="All Ok",
                data={},
            )
            return self.__response(response_data, http_status=status.HTTP_200_OK)
        except SerializerApiException as err:
            response_data = dict(
                success=False,
                message=f"{err}",
                errors=err.errors
            )
            return self.__response(response_data, http_status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            log.exception(f"Error in InstituteUpdaterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
