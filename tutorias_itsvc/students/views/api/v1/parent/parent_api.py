from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.services.parent.controllers import ParentGetterController
from tutorias_itsvc.students.services.parent.controllers import ParentCreatorController
from tutorias_itsvc.students.services.parent.controllers import ParentUpdaterController
from tutorias_itsvc.students.serializers.api.v1.parent import ParentSerializer
from tutorias_itsvc.students.repositories import ParentRepository


class ParentApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request, student_id, type):
        repository = ParentRepository()
        serializer = GetterSerializerService(ParentSerializer)
        response = ResponseService()
        controller = ParentGetterController(
            repository=repository,
            serializer=serializer,
            response=response,
        )
        response = controller(student_id=student_id, type=type)
        return response

    def post(self, request, student_id, type):
        repository = ParentRepository()
        response = ResponseService()
        request = RequestService(request.data, ParentSerializer)
        controller = ParentCreatorController(
            repository=repository,
            request=request,
            response=response,
        )
        response = controller(student_id=student_id, type=type)
        return response

    def put(self, request, student_id, type):
        repository = ParentRepository()
        response = ResponseService()
        request = RequestService(request.data, ParentSerializer)
        controller = ParentUpdaterController(
            repository=repository,
            request=request,
            response=response,
        )
        response = controller(student_id=student_id, type=type)
        return response
