from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.users.services.personal_information import PersonalInformationCreatorService
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.services.student import StudentGetterService

log = get_logger(__file__)


class PersonalInformationCreatorController:
    def __init__(self, request, repository, response, service=None):
        self.__request = request
        self.__repository = repository
        self.__response = response
        self.__service = service or PersonalInformationCreatorService(self.__repository)

    def get_student(self, student_id):
        respository = StudentRepository()
        getter_service = StudentGetterService(respository)
        student = getter_service(id=student_id)
        return student

    def __call__(self, student_id):
        try:
            student = self.get_student(student_id)
            if not student:
                raise Exception("Usuario no existe")
            fields = self.__request.get_data()
            fields.update(dict(user_id=student.user.id))
            self.__service(**fields)
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
