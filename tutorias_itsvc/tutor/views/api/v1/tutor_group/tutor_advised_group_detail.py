from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.responses import ResponseService
from shared.serializers import GetterSerializerService
from tutorias_itsvc.tutor.serializers.api.v1.tutor_group import TutorGroupDetailSerializer
from tutorias_itsvc.tutor.repositories import TutorGroupRepository
from tutorias_itsvc.tutor.services.tutor_group.controllers import TutorGroupGetterController
from tutorias_itsvc.custom_permission import IsTutor
from tutorias_itsvc.custom_permission import IsAdmin


class TutorAdvisedGroupDetailApi(APIView):
    permission_classes = [IsAuthenticated, IsTutor | IsAdmin]

    def get(self, request, tutor_id, advised_group_id):
        repository = TutorGroupRepository()
        serializer = GetterSerializerService(TutorGroupDetailSerializer)
        response = ResponseService()
        getter_controller = TutorGroupGetterController(
            repository=repository,
            serializer=serializer,
            response=response
        )
        response = getter_controller(id=advised_group_id, tutor_id=tutor_id)
        return response
