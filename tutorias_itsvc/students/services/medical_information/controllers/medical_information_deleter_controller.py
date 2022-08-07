from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.repositories import MedicalInformationRepository
from tutorias_itsvc.students.services.medical_information import MedicalInformationDeleterService

log = get_logger(__file__)


class MedicalInformationDeleterController:
    def __init__(self, response, medical_information_repository=None, service=None):
        self.__response = response
        self.__medical_information_repository = medical_information_repository or MedicalInformationRepository()
        self.__service = service or MedicalInformationDeleterService(
            medical_information_repository=self.__medical_information_repository)

    def __call__(self, student_id, medical_information_id):
        try:
            self.__service(medical_information_id=medical_information_id, student_id=student_id)
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
