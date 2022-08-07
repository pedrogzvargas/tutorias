from rest_framework.views import APIView
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from tutorias_itsvc.common.repositories import AcademicDegreeRepository
from tutorias_itsvc.common.serializers.api.v1.academic_degree import AcademicDegreeSerializer
from tutorias_itsvc.common.services.academic_degree.controllers import AcademicDegreeGetterController
from tutorias_itsvc.common.services.academic_degree import AcademicDegreeFilterService


class AcademicDegreesApi(APIView):
    permission_classes = ()

    def get(self, request):
        repository = AcademicDegreeRepository()
        serializer = GetterSerializerService(AcademicDegreeSerializer, many=True)
        response = ResponseService()
        service = AcademicDegreeFilterService(repository)
        getter_controller = AcademicDegreeGetterController(
            repository=repository,
            service=service,
            serializer=serializer,
            response=response
        )
        response = getter_controller()
        return response
