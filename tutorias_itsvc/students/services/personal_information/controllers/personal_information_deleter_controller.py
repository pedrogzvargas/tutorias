from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.services.personal_information import PersonalInformationDeleterService
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.users.repositories import PersonalInformationRepository

log = get_logger(__file__)


class PersonalInformationDeleterController:
    def __init__(self, response, student_repository=None, personal_information_repository=None, deleter_service=None):
        self.__response = response
        self.__student_repository = student_repository or StudentRepository()
        self.__personal_information_repository = personal_information_repository or PersonalInformationRepository()
        self.__service = deleter_service or PersonalInformationDeleterService(
            student_repository=self.__student_repository,
            personal_information_repository=self.__personal_information_repository)

    def __call__(self, student_id):
        try:
            self.__service(student_id)
            response_data = dict(
                success=True,
                message="All Ok",
                data={},
            )
            http_status = status.HTTP_200_OK
            return self.__response(response_data, http_status=http_status)
        except Exception as err:
            log.exception(f"Error in MedicalInformationDeleterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
