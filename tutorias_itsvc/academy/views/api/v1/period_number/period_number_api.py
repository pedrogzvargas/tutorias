from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from tutorias_itsvc.academy.repositories import PeriodNumberRepository
from tutorias_itsvc.academy.serializers.api.v1.period_number import PeriodNumberSerializer
from tutorias_itsvc.academy.services.period_number.controllers import PeriodNumberFilterController
from tutorias_itsvc.utils import query_debugger


class PeriodNumberApi(APIView):
    permission_classes = [AllowAny]

    @query_debugger
    def get(self, request, university_id, major_id, period_id):
        repository = PeriodNumberRepository()
        serializer = GetterSerializerService(PeriodNumberSerializer, True)
        response = ResponseService()
        controller = PeriodNumberFilterController(
            repository=repository,
            serializer=serializer,
            response=response,
        )
        response = controller(
            academic_period_number__academic_period__academic_major__university_id=university_id,
            academic_period_number__academic_period__academic_major__major_id=major_id,
            academic_period_number__academic_period__period__id=period_id
        )
        return response
