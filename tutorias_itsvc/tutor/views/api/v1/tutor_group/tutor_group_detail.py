from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.responses import ResponseService
from shared.serializers import GetterSerializerService
from tutorias_itsvc.tutor.serializers.api.v1.tutor_group import TutorGroupDetailSerializer
from tutorias_itsvc.tutor.repositories import TutorGroupRepository
from tutorias_itsvc.tutor.services.tutor_group.controllers import TutorGroupGetterController


class TutorGroupDetailApi(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, tutor_group_id):
        repository = TutorGroupRepository()
        serializer = GetterSerializerService(TutorGroupDetailSerializer)
        response = ResponseService()
        getter_controller = TutorGroupGetterController(
            repository=repository,
            serializer=serializer,
            response=response
        )
        response = getter_controller(id=tutor_group_id)
        return response
