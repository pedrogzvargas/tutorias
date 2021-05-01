from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from tutorias_itsvc.academy.repositories import GroupRepository
from tutorias_itsvc.academy.serializers.api.v1.group import GroupSerializer
from tutorias_itsvc.academy.services.group.controllers import GroupFilterController
from tutorias_itsvc.utils import query_debugger


class GroupApi(APIView):
    permission_classes = [AllowAny]

    @query_debugger
    def get(self, request, university_id, major_id, period_id, period_number_id):
        repository = GroupRepository()
        serializer = GetterSerializerService(GroupSerializer, True)
        response = ResponseService()
        controller = GroupFilterController(
            repository=repository,
            serializer=serializer,
            response=response
        )
        response = controller(
            academic_group__academic_period_number__academic_period__academic_major__university_id=university_id,
            academic_group__academic_period_number__academic_period__academic_major__major_id=major_id,
            academic_group__academic_period_number__academic_period__period__id=period_id,
            academic_group__academic_period_number__period_number__id=period_number_id,
            academic_group__is_active=True
        )
        return response
