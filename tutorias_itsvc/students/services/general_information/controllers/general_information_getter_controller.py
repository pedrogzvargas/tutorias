from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.services.general_information import GeneralInformationGetterService

log = get_logger(__file__)


class GeneralInformationGetterController:
    def __init__(self, serializer, response, getter_service=None):
        self.__serializer = serializer
        self.__response = response
        self.__service = getter_service

    def __call__(self, user_id):
        try:
            self.__service = self.__service or GeneralInformationGetterService(user_id)
            general_information = self.__service()
            if general_information:
                serializer_data = self.__serializer(general_information)
                response_data = dict(
                    success=True,
                    message="All Ok",
                    data=serializer_data,
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
            log.exception(f"Error in GeneralInformationGetterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
