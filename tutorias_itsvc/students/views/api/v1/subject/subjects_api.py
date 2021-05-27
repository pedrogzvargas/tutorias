from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService

from tutorias_itsvc.students.repositories import StudentSubjectRepository
from tutorias_itsvc.students.serializers.api.v1.subject import SubjectSerializer
from tutorias_itsvc.students.services.student.controllers import StudentGetterController
from tutorias_itsvc.students.services.subject.controllers import SubjectCreatorController
from tutorias_itsvc.students.services.subject import StudentSubjectFilterService


class SubjectsApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request, student_id):
        repository = StudentSubjectRepository()
        service = StudentSubjectFilterService(repository)
        serializer = GetterSerializerService(SubjectSerializer, many=True)
        response = ResponseService()
        controller = StudentGetterController(
            repository=repository,
            service=service,
            serializer=serializer,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def post(self, request, student_id):
        repository = StudentSubjectRepository()
        response = ResponseService()
        request = RequestService(request.data, SubjectSerializer)
        controller = SubjectCreatorController(
            request=request,
            repository=repository,
            response=response,
        )
        response = controller(student_id)
        return response
