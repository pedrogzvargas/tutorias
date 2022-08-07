from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.students.services.subject import StudentSubjectUpdaterService
from tutorias_itsvc.students.services.subject import StudentSubjectGetterService

log = get_logger(__file__)


class SubjectUpdaterController:
    def __init__(self, request, repository, response, service=None):
        self.__request = request
        self.__repository = repository
        self.__response = response
        self.__service = service or StudentSubjectUpdaterService(self.__repository)

    def get_subject(self, student_id, subject_id):
        getter_service = StudentSubjectGetterService(self.__repository)
        subject = getter_service(id=subject_id, student_id=student_id)
        return subject

    def __call__(self, student_id, subject_id):
        try:
            fields = self.__request.get_data()
            subject = self.get_subject(student_id, subject_id)
            if not subject:
                raise Exception('Materia no encontrada')
            fields.update(dict(student_id=student_id))
            self.__service(id=subject.id, **fields)
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
            log.exception(f"Error in SubjectUpdaterController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
