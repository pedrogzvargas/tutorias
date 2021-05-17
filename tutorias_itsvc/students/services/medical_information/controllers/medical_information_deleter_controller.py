from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.repositories import MedicalInformationRepository
from tutorias_itsvc.students.services.medical_information import MedicalInformationGetterService
from tutorias_itsvc.students.services.medical_information import MedicalInformationDeleterService

log = get_logger(__file__)


class MedicalInformationDeleterController:
    def __init__(self, repository, response, deleter_service=None):
        self.__repository = repository
        self.__response = response
        self.__service = deleter_service or MedicalInformationDeleterService(self.__repository)

    def get_medical_information(self, student_id, medical_information_id):
        repository = MedicalInformationRepository()
        getter_service = MedicalInformationGetterService(repository=repository)
        medical_information = getter_service(id=medical_information_id, student_id=student_id)
        return medical_information

    def __call__(self, student_id, medical_information_id):
        try:
            medical_information = self.get_medical_information(student_id, medical_information_id)
            if medical_information:
                self.__service(id=medical_information.id)
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
            log.exception(f"Error in MedicalInformationDeleterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
