from django.db import transaction
from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.tutor.services.tutor import TutorUpdaterService
from tutorias_itsvc.tutor.repositories import TutorRepository
from tutorias_itsvc.users.repositories import UserRepository

log = get_logger(__file__)


class TutorUpdaterController:
    def __init__(self,
                 request,
                 response,
                 tutor_repository=None,
                 user_repository=None,
                 service=None):
        self.__request = request
        self.__response = response
        self.__tutor_repository = tutor_repository or TutorRepository()
        self.__user_repository = user_repository or UserRepository()
        self.__service = service or TutorUpdaterService(tutor_repository=self.__tutor_repository,
                                                        user_repository=self.__user_repository)

    @transaction.atomic
    def __call__(self, tutor_id):
        try:
            fields = self.__request.get_data()
            self.__service(tutor_id=tutor_id, **fields)
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
            log.exception(f"Error in TutorUpdaterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
