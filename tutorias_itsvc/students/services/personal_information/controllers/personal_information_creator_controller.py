from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.common.repositories import GenderRepository
from tutorias_itsvc.common.repositories import MaritalStatusRepository
from tutorias_itsvc.users.repositories import PersonalInformationRepository
from tutorias_itsvc.students.services.personal_information import PersonalInformationCreatorService

log = get_logger(__file__)


class PersonalInformationCreatorController:
    def __init__(self,
                 request,
                 response,
                 personal_information_repository=None,
                 student_repository=None,
                 gender_repository=None,
                 marital_status_repository=None,
                 service=None):
        self.__request = request
        self.__response = response
        self.__personal_information_repository = personal_information_repository or PersonalInformationRepository()
        self.__student_repository = student_repository or StudentRepository()
        self.__gender_repository = gender_repository or GenderRepository()
        self.__marital_status_repository = marital_status_repository or MaritalStatusRepository()
        self.__service = service or PersonalInformationCreatorService(
            personal_information_repository=self.__personal_information_repository,
            student_repository=self.__student_repository,
            gender_repository=self.__gender_repository,
            marital_status_repository=self.__marital_status_repository,
        )

    def __call__(self, student_id):
        try:
            fields = self.__request.get_data()
            self.__service(student_id=student_id, **fields)
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
            log.exception(f"Error in PersonalInformationCreatorController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
