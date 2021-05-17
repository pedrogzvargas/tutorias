from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.students.services.medical_information import MedicalInformationUpdaterService
from tutorias_itsvc.students.services.medical_information import MedicalInformationGetterService

log = get_logger(__file__)


class MedicalInformationUpdaterController:
    def __init__(self, request, repository, response, service=None):
        self.__request = request
        self.__repository = repository
        self.__response = response
        self.__service = service or MedicalInformationUpdaterService(self.__repository)

    def get_medical_information(self, student_id, medical_information_id):
        getter_service = MedicalInformationGetterService(self.__repository)
        medical_information = getter_service(id=medical_information_id, student_id=student_id)
        return medical_information

    def __call__(self, student_id, medical_information_id):
        try:
            fields = self.__request.get_data()
            fields.update(dict(student_id=student_id))
            medical_information = self.get_medical_information(student_id, medical_information_id)
            if not medical_information:
                raise Exception("Medical information not exist")
            self.__service(id=medical_information_id, **fields)
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
            log.exception(f"Error in MedicalInformationUpdatorController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
