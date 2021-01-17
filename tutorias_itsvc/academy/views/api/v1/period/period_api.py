from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from tutorias_itsvc.academy.repositories import PeriodRepository
from tutorias_itsvc.academy.serializers.api.v1.period import PeriodSerializer
from tutorias_itsvc.academy.services.period.controllers import PeriodFilterController
from tutorias_itsvc.utils import query_debugger


class PeriodApi(APIView):
    permission_classes = [AllowAny]

    @query_debugger
    def get(self, request, university_id, major_id):
        repository = PeriodRepository()
        serializer = GetterSerializerService(PeriodSerializer, True)
        response = ResponseService()
        controller = PeriodFilterController(
            repository=repository,
            serializer=serializer,
            response=response,
        )
        response = controller(
            academic_period__academic_major__university_id=university_id,
            academic_period__academic_major__major_id=major_id)
        return response
