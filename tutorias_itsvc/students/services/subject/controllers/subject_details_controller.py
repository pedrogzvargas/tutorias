from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.repositories import StudentSubjectRepository
from tutorias_itsvc.academy.repositories import AcademicSubjectRepository
from tutorias_itsvc.students.repositories import AcademicInformationRepository
from tutorias_itsvc.students.services.subject import StudentSubjectDetailsService

log = get_logger(__file__)


class SubjectDetailsController:
    def __init__(self,
                 serializer,
                 response,
                 student_repository=None,
                 academic_subject_repository=None,
                 student_subject_repository=None,
                 academic_information_repository=None,
                 service=None):
        self.__serializer = serializer
        self.__response = response
        self.__student_repository = student_repository or StudentRepository()
        self.__academic_subject_repository = academic_subject_repository or AcademicSubjectRepository()
        self.__student_subject_repository = student_subject_repository or StudentSubjectRepository()
        self.__academic_information_repository = academic_information_repository or AcademicInformationRepository()
        self.__service = service or StudentSubjectDetailsService(
            student_repository=self.__student_repository,
            academic_subject_repository=self.__academic_subject_repository,
            student_subject_repository=self.__student_subject_repository,
            academic_information_repository=self.__academic_information_repository,
        )

    def __call__(self, student_id):
        try:
            details = self.__service(student_id)
            serializer_data = self.__serializer(details)
            response_data = dict(
                success=True,
                message="All Ok",
                data=serializer_data,
            )
            http_status = status.HTTP_200_OK
            return self.__response(response_data, http_status=http_status)
        except Exception as err:
            log.exception(f"Error in SubjectDetailsController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
