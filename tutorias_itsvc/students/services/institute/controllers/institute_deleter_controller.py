from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.repositories import StudentInstituteRepository
from tutorias_itsvc.students.services.institute import InstituteGetterService
from tutorias_itsvc.students.services.institute import InstituteDeleterService

log = get_logger(__file__)


class InstituteDeleterController:
    def __init__(self, repository, response, deleter_service=None):
        self.__repository = repository
        self.__response = response
        self.__service = deleter_service or InstituteDeleterService(self.__repository)

    def get_institute(self, student_id, institute_id):
        repository = StudentInstituteRepository()
        getter_service = InstituteGetterService(repository=repository)
        institute = getter_service(id=institute_id, student_id=student_id)
        return institute

    def __call__(self, student_id, institute_id):
        try:
            institute = self.get_institute(student_id, institute_id)
            if institute:
                self.__service(id=institute.id)
                response_data = dict(
                    success=True,
                    message="All Ok",
                    data={},
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
            log.exception(f"Error in InstituteDeleterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
