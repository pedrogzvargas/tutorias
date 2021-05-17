from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.students.services.academic_information import AcademicInformationUpdaterService
from tutorias_itsvc.students.services.academic_information import AcademicInformationGetterService
from tutorias_itsvc.academy.repositories import AcademicGroupRepository
from tutorias_itsvc.academy.services.academic_group import AcademicGroupGetterService

log = get_logger(__file__)


class AcademicInformationUpdaterController:
    def __init__(self, request, repository, response, updater_service=None):
        self.__request = request
        self.__repository = repository
        self.__response = response
        self.__updater_service = updater_service or AcademicInformationUpdaterService(self.__repository)

    def get_academic(self, university_id, major_id, period_id, group_id, period_number_id):
        repository = AcademicGroupRepository()
        getter_service = AcademicGroupGetterService(repository)
        academic = getter_service(
            academic_period_number__academic_period__academic_major__university_id=university_id,
            academic_period_number__academic_period__academic_major__major_id=major_id,
            academic_period_number__academic_period__period_id=period_id,
            academic_period_number__period_number_id=period_number_id,
            group_id=group_id
        )
        return academic

    def get_academic_information(self, student_id, academic_information_id):
        getter_service = AcademicInformationGetterService(self.__repository)
        academic_information = getter_service(id=academic_information_id, student_id=student_id, is_active=True)
        return academic_information

    def __call__(self, student_id, academic_information_id):
        try:
            fields = self.__request.get_data()
            academic_information = self.get_academic_information(student_id, academic_information_id)
            if not academic_information:
                raise Exception("No existe un registro para actualizar")
            academic = self.get_academic(
                university_id=fields.get("university_id"),
                major_id=fields.get("major_id"),
                period_id=fields.get("period_id"),
                group_id=fields.get("group_id"),
                period_number_id=fields.get("period_number_id")
            )
            if not academic:
                raise Exception("No existe la información academica")
            self.__updater_service(id=academic_information.id, student_id=student_id, academic_information_id=academic.id)
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
            log.exception(f"Error in AcademicInformationCreatorController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",

            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
