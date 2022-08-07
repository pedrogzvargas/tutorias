from rest_framework.views import APIView
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from tutorias_itsvc.common.repositories import HomeStatusRepository
from tutorias_itsvc.common.serializers.api.v1.home_satus import HomeStatusSerializer
from tutorias_itsvc.common.services.home_status.controllers import HomeStatusGetterController
from tutorias_itsvc.common.services.home_status import HomeStatusFilterService


class HomesStatusApi(APIView):
    permission_classes = ()

    def get(self, request):
        repository = HomeStatusRepository()
        serializer = GetterSerializerService(HomeStatusSerializer, many=True)
        response = ResponseService()
        service = HomeStatusFilterService(repository)
        getter_controller = HomeStatusGetterController(
            repository=repository,
            service=service,
            serializer=serializer,
            response=response
        )
        response = getter_controller()
        return response
