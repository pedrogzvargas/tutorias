from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.users.serializers.api.v1.sibling import SiblingSerializer
from tutorias_itsvc.students.repositories import StudentSiblingRepository
from tutorias_itsvc.students.services.siblings.controllers import SiblingCreatorController
from tutorias_itsvc.students.services.siblings.controllers import SiblingFilterController


class SiblingsApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request, student_id):
        repository = StudentSiblingRepository()
        serializer = GetterSerializerService(SiblingSerializer, many=True)
        response = ResponseService()
        controller = SiblingFilterController(
            repository=repository,
            serializer=serializer,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def post(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, SiblingSerializer)
        controller = SiblingCreatorController(
            request=request,
            response=response,
        )
        response = controller(student_id)
        return response
