from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.students.services.medical_information import MedicalInformationCreatorService
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.repositories import MedicalInformationRepository
from tutorias_itsvc.common.repositories import DisabilityRepository

log = get_logger(__file__)


class MedicalInformationCreatorController:
    def __init__(self,
                 request,
                 response,
                 medical_information_repository=None,
                 student_repository=None,
                 disability_repository=None,
                 service=None):
        self.__request = request
        self.__response = response
        self.__medical_information_repository = medical_information_repository or MedicalInformationRepository()
        self.__student_repository = student_repository or StudentRepository()
        self.__disability_repository = disability_repository or DisabilityRepository()
        self.__service = service or MedicalInformationCreatorService(
            medical_information_repository=self.__medical_information_repository,
            student_repository=self.__student_repository,
            disability_repository=self.__disability_repository,
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
            log.exception(f"Error in MedicalInformationCreatorController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
