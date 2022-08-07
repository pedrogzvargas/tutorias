from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.services.estado_psicofisiologico import EstadoPsicofisiologicoDeleterService
from tutorias_itsvc.students.repositories import EstadoPsicofisiologicoRepository
from tutorias_itsvc.students.repositories import StudentRepository

log = get_logger(__file__)


class EstadoPsicofisiologicoDeleterController:
    def __init__(self,
                 response,
                 estado_psicofisiologico_repository=None,
                 student_repository=None,
                 service=None):
        self.__response = response
        self.__estado_psicofisiologico_repository = estado_psicofisiologico_repository or EstadoPsicofisiologicoRepository()
        self.__student_repository = student_repository or StudentRepository()
        self.__service = service or EstadoPsicofisiologicoDeleterService(
            estado_psicofisiologico_repository=self.__estado_psicofisiologico_repository,
            student_repository=self.__student_repository
        )

    def __call__(self, student_id):
        try:
            self.__service(student_id=student_id)
            response_data = dict(
                success=True,
                message="All Ok",
                data={},
            )
            return self.__response(response_data, http_status=status.HTTP_200_OK)
        except Exception as err:
            log.exception(f"Error in EstadoPsicofisiologicoDeleterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
