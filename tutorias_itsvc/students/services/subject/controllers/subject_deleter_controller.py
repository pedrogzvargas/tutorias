from rest_framework import status
from shared.utils import get_logger
from tutorias_itsvc.students.services.subject import StudentSubjectGetterService
from tutorias_itsvc.students.services.subject import StudentSubjectDeleterService

log = get_logger(__file__)


class SubjectDeleterController:
    def __init__(self, repository, response, getter_service=None):
        self.__repository = repository
        self.__response = response
        self.__service = getter_service or StudentSubjectDeleterService(self.__repository)

    def get_subject(self, student_id, subject_id):
        getter_service = StudentSubjectGetterService(self.__repository)
        subject = getter_service(id=subject_id, student_id=student_id)
        return subject

    def __call__(self, student_id, subject_id):
        try:
            subject = self.get_subject(student_id, subject_id)
            if subject:
                self.__service(subject.id)
                response_data = dict(
                    success=True,
                    message="All Ok",
                    data={},
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
            log.exception(f"Error in SubjectDeleterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
