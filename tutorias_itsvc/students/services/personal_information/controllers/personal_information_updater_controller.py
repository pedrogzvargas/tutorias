from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.students.services.medical_information import MedicalInformationUpdaterService
from tutorias_itsvc.users.services.personal_information import PersonalInformationGetterService
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.services.student import StudentGetterService
from tutorias_itsvc.users.repositories import PersonalInformationRepository

log = get_logger(__file__)


class PersonalInformationUpdaterController:
    def __init__(self, request, repository, response, service=None):
        self.__request = request
        self.__repository = repository
        self.__response = response
        self.__service = service or MedicalInformationUpdaterService(self.__repository)

    def get_student(self, student_id):
        respository = StudentRepository()
        getter_service = StudentGetterService(respository)
        student = getter_service(id=student_id)
        return student

    def get_personal_information(self, user_id):
        repository = PersonalInformationRepository()
        getter_service = PersonalInformationGetterService(repository)
        personal_information = getter_service(user_id=user_id)
        return personal_information

    def __call__(self, student_id):
        try:
            fields = self.__request.get_data()
            student = self.get_student(student_id)
            if not student:
                raise Exception("Usuario no existe")
            personal_information = self.get_personal_information(student.user.id)
            if not personal_information:
                raise Exception("Personal information not exist")
            self.__service(id=personal_information.id, **fields)
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
            log.exception(f"Error in MedicalInformationUpdatorController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
