from rest_framework.views import APIView
from rest_framework.permissions import AllowAny

from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService

from tutorias_itsvc.students.repositories import StudentSubjectRepository
from tutorias_itsvc.students.serializers.api.v1.subject import SubjectSerializer
from tutorias_itsvc.students.services.student.controllers import StudentGetterController
from tutorias_itsvc.students.services.subject.controllers import SubjectUpdaterController
from tutorias_itsvc.students.services.subject.controllers import SubjectDeleterController


class SubjectApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request, student_id, subject_id):
        repository = StudentSubjectRepository()
        serializer = GetterSerializerService(SubjectSerializer)
        response = ResponseService()
        controller = StudentGetterController(
            repository=repository,
            serializer=serializer,
            response=response,
        )
        response = controller(id=subject_id, student_id=student_id)
        return response

    def put(self, request, student_id, subject_id):
        repository = StudentSubjectRepository()
        response = ResponseService()
        request = RequestService(request.data, SubjectSerializer)
        controller = SubjectUpdaterController(
            request=request,
            repository=repository,
            response=response,
        )
        response = controller(student_id, subject_id)
        return response

    def delete(self, request, student_id, subject_id):
        repository = StudentSubjectRepository()
        response = ResponseService()
        controller = SubjectDeleterController(
            repository=repository,
            response=response,
        )
        response = controller(student_id, subject_id)
        return response
