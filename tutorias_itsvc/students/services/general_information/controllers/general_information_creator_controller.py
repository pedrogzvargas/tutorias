from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.students.services.general_information import GeneralInformationCreatorService

log = get_logger(__file__)


class GeneralInformationCreatorController:
    def __init__(self, request, response, creator_service=None):
        self.__request = request
        self.__response = response
        self.__creator_service = creator_service

    def __call__(self, user_id):
        try:
            fields = self.__request.get_data()
            self.__creator_service = self.__creator_service or GeneralInformationCreatorService(user_id)
            self.__creator_service(**fields)
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
            log.exception(f"Error in GeneralInformationCreatorController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",

            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
