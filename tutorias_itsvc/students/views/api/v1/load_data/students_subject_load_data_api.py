from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.responses import ResponseService
from shared.requests import RequestService

from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.repositories import StudentSubjectRepository
from tutorias_itsvc.tutor.repositories import TutorSubjectRepository
from tutorias_itsvc.academy.repositories import SubjectTypeRepository
from tutorias_itsvc.common.repositories import SchoolCycleRepository
from tutorias_itsvc.academy.repositories import SubjectFailureMetricRepository
from tutorias_itsvc.students.serializers.api.v1.load_data import StudentsSubjectLoadDataSerializer
from tutorias_itsvc.students.services.load_data.controllers import StudentsSubjectLoaderController
from tutorias_itsvc.custom_permission import IsTutor
from tutorias_itsvc.custom_permission import IsAdmin


class StudentsSubjectLoadDataApi(APIView):
    permission_classes = [IsAuthenticated, IsTutor | IsAdmin]

    def post(self, request):
        student_repository = StudentRepository()
        student_subject_repository = StudentSubjectRepository()
        tutor_subject_repository = TutorSubjectRepository()
        subject_type_repository = SubjectTypeRepository()
        school_cycle_repository = SchoolCycleRepository()
        failed_metric_repository = SubjectFailureMetricRepository()
        response = ResponseService()
        request = RequestService(request.data, StudentsSubjectLoadDataSerializer)
        controller = StudentsSubjectLoaderController(
            student_repository=student_repository,
            student_subject_repository=student_subject_repository,
            tutor_subject_repository=tutor_subject_repository,
            subject_type_repository=subject_type_repository,
            school_cycle_repository=school_cycle_repository,
            failed_metric_repository=failed_metric_repository,
            request=request,
            response=response,
        )
        response = controller()
        return response
