from rest_framework.views import APIView
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from tutorias_itsvc.common.repositories import MaritalStatusRepository
from tutorias_itsvc.common.serializers.api.v1.marital_status import MaritalStatusSerializer
from tutorias_itsvc.common.services.marital_status.controllers import MaritalStatusGetterController
from tutorias_itsvc.common.services.marital_status import MaritalStatusFilterService


class MaritalStatusesApi(APIView):
    permission_classes = ()

    def get(self, request):
        repository = MaritalStatusRepository()
        serializer = GetterSerializerService(MaritalStatusSerializer, many=True)
        response = ResponseService()
        service = MaritalStatusFilterService(repository)
        getter_controller = MaritalStatusGetterController(
            repository=repository,
            service=service,
            serializer=serializer,
            response=response
        )
        response = getter_controller()
        return response
