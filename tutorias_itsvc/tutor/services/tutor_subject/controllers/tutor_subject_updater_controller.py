from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.tutor.services.tutor_subject import TutorSubjectUpdaterService


log = get_logger(__file__)


class TutorSubjectUpdaterController:
    def __init__(self, request, repository, response, service=None):
        self.__request = request
        self.__repository = repository
        self.__response = response
        self.__service = service or TutorSubjectUpdaterService(self.__repository)

    def __call__(self, tutor_subject_id):
        try:
            fields = self.__request.get_data()
            if not self.__repository.get(id=tutor_subject_id):
                raise Exception("No existe el registro")
            self.__service(tutor_subject_id, **fields)
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
            log.exception(f"Error in TutorSubjectUpdaterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
