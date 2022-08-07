from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.repositories import StudentInstituteRepository
from tutorias_itsvc.students.services.institute import InstituteDeleterService

log = get_logger(__file__)


class InstituteDeleterController:
    def __init__(self, response, student_institute_repository=None, deleter_service=None):
        self.__response = response
        self.__student_institute_repository = student_institute_repository or StudentInstituteRepository()
        self.__service = deleter_service or InstituteDeleterService(
            student_institute_repository=self.__student_institute_repository)

    def __call__(self, student_id, institute_id):
        try:
            self.__service(institute_id=institute_id, student_id=student_id)
            response_data = dict(
                    success=True,
                    message="All Ok",
                    data={},
                )
            http_status = status.HTTP_200_OK
            return self.__response(response_data, http_status=http_status)
        except Exception as err:
            log.exception(f"Error in InstituteDeleterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
