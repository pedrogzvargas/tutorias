from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.students.services.academic_information import AcademicInformationUpdaterService
from tutorias_itsvc.students.services.academic_information.exceptions import AcademicInformationNotExist
from tutorias_itsvc.students.repositories import AcademicInformationRepository
from tutorias_itsvc.academy.repositories import AcademicGroupRepository

log = get_logger(__file__)


class AcademicInformationUpdaterController:
    def __init__(self,
                 request,
                 response,
                 academic_information_repository=None,
                 academic_group_repository=None,
                 service=None):
        self.__request = request
        self.__response = response
        self.__academic_information_repository = academic_information_repository or AcademicInformationRepository()
        self.__academic_group_repository = academic_group_repository or AcademicGroupRepository()
        self.__service = service or AcademicInformationUpdaterService(
            academic_information_repository=self.__academic_information_repository,
            academic_group_repository=self.__academic_group_repository
        )

    def __call__(self, student_id, academic_information_id):
        try:
            fields = self.__request.get_data()
            self.__service(student_id=student_id, academic_information_id=academic_information_id, **fields)
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

        except AcademicInformationNotExist as err:
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_400_BAD_REQUEST)

        except Exception as err:
            log.exception(f"Error in AcademicInformationCreatorController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",

            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
