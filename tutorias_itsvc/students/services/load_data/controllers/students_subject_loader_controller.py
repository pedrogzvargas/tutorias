from django.db import transaction
from rest_framework import status
from shared.utils import get_logger
from shared.exceptions import SerializerApiException
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.tutor.repositories import TutorSubjectRepository
from tutorias_itsvc.students.repositories import StudentSubjectRepository
from tutorias_itsvc.academy.repositories import SubjectTypeRepository
from tutorias_itsvc.academy.repositories import SubjectFailureMetricRepository
from tutorias_itsvc.common.repositories import SchoolCycleRepository
from tutorias_itsvc.students.services.load_data import StudentsSubjectLoaderService

log = get_logger(__file__)


class StudentsSubjectLoaderController:
    def __init__(
        self,
        request,
        response,
        student_repository=None,
        student_subject_repository=None,
        tutor_subject_repository=None,
        subject_type_repository=None,
        school_cycle_repository=None,
        failed_metric_repository=None,
        service=None
    ):
        self.__request = request
        self.__response = response
        self.__student_repository = student_repository or StudentRepository()
        self.__student_subject_repository = student_subject_repository or StudentSubjectRepository()
        self.__tutor_subject_repository = tutor_subject_repository or TutorSubjectRepository()
        self.__subject_type_repository = subject_type_repository or SubjectTypeRepository()
        self.__school_cycle_repository = school_cycle_repository or SchoolCycleRepository()
        self.__failed_metric_repository = failed_metric_repository or SubjectFailureMetricRepository()
        self.__service = service or StudentsSubjectLoaderService(student_repository=self.__student_repository,
                                                                 student_subject_repository=self.__student_subject_repository,
                                                                 tutor_subject_repository=self.__tutor_subject_repository,
                                                                 subject_type_repository=self.__subject_type_repository,
                                                                 school_cycle_repository=self.__school_cycle_repository,
                                                                 failed_metric_repository=self.__failed_metric_repository,
                                                                 )

    @transaction.atomic
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
            log.exception(f"Error in StudentsSubjectLoaderController::__call__, error: {err}")
            response_data = dict(
                success=False,
                message=f"{err}",
            )
            return self.__response(response_data, http_status=status.HTTP_500_INTERNAL_SERVER_ERROR)
