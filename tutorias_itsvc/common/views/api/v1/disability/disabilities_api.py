from rest_framework.views import APIView
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from tutorias_itsvc.common.repositories import DisabilityRepository
from tutorias_itsvc.common.serializers.api.v1.disability import DisabilitySerializer
from tutorias_itsvc.common.services.disability.controllers import DisabilityGetterController
from tutorias_itsvc.common.services.disability import DisabilityFilterService


class DisabilitiesApi(APIView):
    permission_classes = ()

    def get(self, request):
        repository = DisabilityRepository()
        serializer = GetterSerializerService(DisabilitySerializer, many=True)
        response = ResponseService()
        service = DisabilityFilterService(repository)
        getter_controller = DisabilityGetterController(
            repository=repository,
            service=service,
            serializer=serializer,
            response=response
        )
        response = getter_controller()
        return response
