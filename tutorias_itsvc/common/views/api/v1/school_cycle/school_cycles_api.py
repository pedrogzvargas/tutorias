from rest_framework.views import APIView
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from tutorias_itsvc.common.repositories import SchoolCycleRepository
from tutorias_itsvc.common.serializers.api.v1.school_cycle import SchoolCycleSerializer
from tutorias_itsvc.common.services.school_cycle.controllers import SchoolCycleGetterController
from tutorias_itsvc.common.services.school_cycle import SchoolCycleFilterService


class SchoolCyclesApi(APIView):
    permission_classes = ()

    def get(self, request):
        repository = SchoolCycleRepository()
        serializer = GetterSerializerService(SchoolCycleSerializer, many=True)
        response = ResponseService()
        service = SchoolCycleFilterService(repository)
        getter_controller = SchoolCycleGetterController(
            repository=repository,
            service=service,
            serializer=serializer,
            response=response
        )
        response = getter_controller()
        return response
