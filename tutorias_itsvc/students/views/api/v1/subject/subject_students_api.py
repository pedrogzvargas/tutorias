from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from tutorias_itsvc.students.repositories import StudentSubjectRepository
from tutorias_itsvc.students.serializers.api.v1.subject import StudentSubjectSerializer
from tutorias_itsvc.students.services.subject.controllers import SubjectFilterController
from tutorias_itsvc.custom_permission import IsTutor
from tutorias_itsvc.custom_permission import IsAdmin


class SubjectStudentsApi(APIView):
    permission_classes = [IsAuthenticated, IsTutor | IsAdmin]

    def get(self, request, tutor_subject_id):
        repository = StudentSubjectRepository()
        serializer = GetterSerializerService(StudentSubjectSerializer, many=True)
        response = ResponseService()
        controller = SubjectFilterController(
            request=request,
            repository=repository,
            serializer=serializer,
            response=response,
        )
        response = controller(tutor_subject_id=tutor_subject_id)
        return response
