from rest_framework.views import APIView
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from tutorias_itsvc.common.repositories import GenderRepository
from tutorias_itsvc.common.serializers.api.v1.gender import GenderSerializer
from tutorias_itsvc.common.services.gender.controllers import GenderGetterController
from tutorias_itsvc.common.services.gender import GenderFilterService


class GendersApi(APIView):
    permission_classes = ()

    def get(self, request):
        repository = GenderRepository()
        serializer = GetterSerializerService(GenderSerializer, many=True)
        response = ResponseService()
        service = GenderFilterService(repository)
        getter_controller = GenderGetterController(
            repository=repository,
            service=service,
            serializer=serializer,
            response=response
        )
        response = getter_controller()
        return response
