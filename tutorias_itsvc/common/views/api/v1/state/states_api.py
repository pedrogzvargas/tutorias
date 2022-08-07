from rest_framework.views import APIView
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from tutorias_itsvc.common.repositories import StateRepository
from tutorias_itsvc.common.serializers.api.v1.state import StateSerializer
from tutorias_itsvc.common.services.state.controllers import StateGetterController
from tutorias_itsvc.common.services.state import StateFilterService


class StatesApi(APIView):
    permission_classes = ()

    def get(self, request):
        repository = StateRepository()
        serializer = GetterSerializerService(StateSerializer, many=True)
        response = ResponseService()
        service = StateFilterService(repository)
        getter_controller = StateGetterController(
            repository=repository,
            service=service,
            serializer=serializer,
            response=response
        )
        response = getter_controller()
        return response
