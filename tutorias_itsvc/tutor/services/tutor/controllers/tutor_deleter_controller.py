from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.tutor.repositories import TutorRepository
from tutorias_itsvc.users.repositories import UserRepository
from tutorias_itsvc.tutor.services.tutor import TutorDeleterService

log = get_logger(__file__)


class TutorDeleterController:
    def __init__(self, response, tutor_repository=None, user_repository=None, service=None):
        self.__response = response
        self.__tutor_repository = tutor_repository or TutorRepository()
        self.__user_repository = user_repository or UserRepository()
        self.__service = service or TutorDeleterService(tutor_repository=self.__tutor_repository,
                                                        user_repository=self.__user_repository)

    def __call__(self, tutor_id):
        try:
            self.__service(tutor_id=tutor_id)
            response_data = dict(
                    success=True,
                    message="All Ok",
                    data={},
                )
            http_status = status.HTTP_200_OK
            return self.__response(response_data, http_status=http_status)
        except Exception as err:
            log.exception(f"Error in TutorDeleterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
