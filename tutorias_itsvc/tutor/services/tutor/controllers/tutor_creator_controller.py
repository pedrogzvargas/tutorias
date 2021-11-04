from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.tutor.services.tutor import TutorCreatorService
from tutorias_itsvc.tutor.repositories import TutorRepository
from tutorias_itsvc.users.repositories import UserRepository
from tutorias_itsvc.users.repositories import GroupRepository

log = get_logger(__file__)


class TutorCreatorController:
    def __init__(self,
                 request,
                 response,
                 tutor_repository=None,
                 user_repository=None,
                 group_repository=None,
                 service=None):
        self.__request = request
        self.__response = response
        self.__tutor_repository = tutor_repository or TutorRepository()
        self.__user_repository = user_repository or UserRepository()
        self.__group_repository = group_repository or GroupRepository()
        self.__service = service or TutorCreatorService(tutor_repository=self.__tutor_repository,
                                                        user_repository=self.__user_repository,
                                                        group_repository=self.__group_repository)

    def __call__(self):
        try:
            fields = self.__request.get_data()
            self.__service(**fields)
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
            log.exception(f"Error in TutorCreatorController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
