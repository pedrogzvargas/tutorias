from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from tutorias_itsvc.academy.repositories import SubjectFailureMetricRepository
from tutorias_itsvc.academy.serializers.api.v1.subject_failure_metric import SubjectFailureMetricSerializer
from tutorias_itsvc.academy.services.subject_failure_metric.controllers import SubjectFailureMetricGetterController
from tutorias_itsvc.academy.services.subject_failure_metric import SubjectFailureMetricFilterService
from tutorias_itsvc.utils import query_debugger


class SubjectFailureMetricsApi(APIView):
    permission_classes = [AllowAny]

    @query_debugger
    def get(self, request):
        repository = SubjectFailureMetricRepository()
        service = SubjectFailureMetricFilterService(repository)
        serializer = GetterSerializerService(SubjectFailureMetricSerializer, True)
        response = ResponseService()
        controller = SubjectFailureMetricGetterController(
            service=service,
            repository=repository,
            serializer=serializer,
            response=response
        )
        response = controller()
        return response
