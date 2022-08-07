from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.services.interview_evaluation import InterviewEvaluationGetterService

log = get_logger(__file__)


class InterviewEvaluationGetterController:
    def __init__(
        self,
        request,
        student_repository,
        organizacion_estudio_repository,
        tecnica_estudio_repository,
        motivacion_estudio_repository,
        estilo_aprendizaje_repository,
        serializer,
        response,
        getter_service=None
    ):
        self.__request = request
        self.__student_repository = student_repository
        self.__organizacion_estudio_repository = organizacion_estudio_repository
        self.__tecnica_estudio_repository = tecnica_estudio_repository
        self.__motivacion_estudio_repository = motivacion_estudio_repository
        self.__estilo_aprendizaje_repository = estilo_aprendizaje_repository
        self.__serializer = serializer
        self.__response = response
        self.__service = getter_service or InterviewEvaluationGetterService(
            request=self.__request,
            student_repository=self.__student_repository,
            organizacion_estudio_repository=self.__organizacion_estudio_repository,
            tecnica_estudio_repository=self.__tecnica_estudio_repository,
            motivacion_estudio_repository=self.__motivacion_estudio_repository,
            estilo_aprendizaje_repository=self.__estilo_aprendizaje_repository,
        )

    def __call__(self, student_id):
        try:
            interview = self.__service(student_id=student_id)
            if interview:
                serializer_data = self.__serializer(interview)
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
            log.exception(f"Error in InterviewEvaluationGetterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
