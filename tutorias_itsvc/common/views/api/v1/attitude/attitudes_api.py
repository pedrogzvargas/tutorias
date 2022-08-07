from rest_framework.views import APIView
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from tutorias_itsvc.common.repositories import AttitudeRepository
from tutorias_itsvc.common.serializers.api.v1.attitude import AttitudeSerializer
from tutorias_itsvc.common.services.attitude.controllers import AttitudeGetterController
from tutorias_itsvc.common.services.attitude import AttitudeFilterService


class AttitudesApi(APIView):
    permission_classes = ()

    def get(self, request):
        repository = AttitudeRepository()
        serializer = GetterSerializerService(AttitudeSerializer, many=True)
        response = ResponseService()
        service = AttitudeFilterService(repository)
        getter_controller = AttitudeGetterController(
            repository=repository,
            service=service,
            serializer=serializer,
            response=response
        )
        response = getter_controller()
        return response
