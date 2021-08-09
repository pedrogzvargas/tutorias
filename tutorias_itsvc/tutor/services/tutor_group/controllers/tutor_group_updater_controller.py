from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.tutor.services.tutor_group import TutorGroupUpdaterService
from tutorias_itsvc.academy.services.academic_group import AcademicGroupGetterService


log = get_logger(__file__)


class TutorGroupUpdaterController:
    def __init__(self, request, tutor_group_repository, academic_group_repository, response, service=None):
        self.__request = request
        self.__tutor_group_repository = tutor_group_repository
        self.__academic_group_repository = academic_group_repository
        self.__response = response
        self.__service = service or TutorGroupUpdaterService(self.__tutor_group_repository)

    def get_academic(self, university_id, major_id, period_id, group_id, period_number_id):
        getter_service = AcademicGroupGetterService(self.__academic_group_repository)
        academic = getter_service(
            academic_period_number__academic_period__academic_major__university_id=university_id,
            academic_period_number__academic_period__academic_major__major_id=major_id,
            academic_period_number__academic_period__period_id=period_id,
            academic_period_number__period_number_id=period_number_id,
            group_id=group_id
        )
        return academic

    def __call__(self, tutor_group_id):
        try:
            fields = self.__request.get_data()
            if not self.__tutor_group_repository.get(id=tutor_group_id):
                raise Exception("No existe el registro")
            academic = self.get_academic(
                university_id=fields.get("university_id"),
                major_id=fields.get("major_id"),
                period_id=fields.get("period_id"),
                group_id=fields.get("group_id"),
                period_number_id=fields.get("period_number_id")
            )
            if not academic:
                raise Exception("No existe la información academica")
            fields = dict(
                tutor_id=fields.get("tutor_id"),
                academic_group_id=academic.id,
                school_cycle_id=fields.get("school_cycle_id"),
            )
            self.__service(tutor_group_id, **fields)
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
            log.exception(f"Error in TutorGroupUpdaterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
