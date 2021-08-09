from rest_framework.views import APIView
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from tutorias_itsvc.common.repositories import RelationshipRepository
from tutorias_itsvc.common.serializers.api.v1.relationship import RelationshipSerializer
from tutorias_itsvc.common.services.relationship.controllers import RelationshipGetterController
from tutorias_itsvc.common.services.relationship import RelationshipFilterService


class RelationshipsApi(APIView):
    permission_classes = ()

    def get(self, request):
        repository = RelationshipRepository()
        serializer = GetterSerializerService(RelationshipSerializer, many=True)
        response = ResponseService()
        service = RelationshipFilterService(repository)
        getter_controller = RelationshipGetterController(
            repository=repository,
            service=service,
            serializer=serializer,
            response=response
        )
        response = getter_controller()
        return response
