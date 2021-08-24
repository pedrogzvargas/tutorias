from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.responses import ResponseService
from shared.serializers import GetterSerializerService
from tutorias_itsvc.tutor.serializers.api.v1.tutor_subject import TutorSubjectDetailSerializer
from tutorias_itsvc.tutor.repositories import TutorSubjectRepository
from tutorias_itsvc.tutor.services.tutor_subject.controllers import TutorSubjectGetterController


class TaughtSubjectDetailApi(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, taught_subject_id):
        repository = TutorSubjectRepository()
        serializer = GetterSerializerService(TutorSubjectDetailSerializer)
        response = ResponseService()
        getter_controller = TutorSubjectGetterController(
            repository=repository,
            serializer=serializer,
            response=response
        )
        response = getter_controller(id=taught_subject_id)
        return response
