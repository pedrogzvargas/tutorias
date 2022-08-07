from rest_framework.views import APIView
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from tutorias_itsvc.common.repositories import HousingTypeRepository
from tutorias_itsvc.common.serializers.api.v1.housing_type import HousingTypeSerializer
from tutorias_itsvc.common.services.housing_type.controllers import HousingTypeGetterController
from tutorias_itsvc.common.services.housing_type import HousingTypeFilterService


class HousingsTypeApi(APIView):
    permission_classes = ()

    def get(self, request):
        repository = HousingTypeRepository()
        serializer = GetterSerializerService(HousingTypeSerializer, many=True)
        response = ResponseService()
        service = HousingTypeFilterService(repository)
        getter_controller = HousingTypeGetterController(
            repository=repository,
            service=service,
            serializer=serializer,
            response=response
        )
        response = getter_controller()
        return response
