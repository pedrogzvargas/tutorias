from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.repositories import StudentJobRepository
from tutorias_itsvc.students.services.job import StudentJobGetterService

log = get_logger(__file__)


class StudentJobGetterController:
    def __init__(self, response, serializer, student_job_repository=None, service=None):
        self.__response = response
        self.__serializer = serializer
        self.__student_job_repository = student_job_repository or StudentJobRepository()
        self.__service = service or StudentJobGetterService(repository=self.__student_job_repository)

    def __call__(self, **kwargs):
        try:
            job = self.__service(**kwargs)
            if job:
                serializer_data = self.__serializer(job)
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
            log.exception(f"Error in IncomeGetterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
