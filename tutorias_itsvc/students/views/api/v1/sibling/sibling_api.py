from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.users.serializers.api.v1.sibling import SiblingSerializer
from tutorias_itsvc.students.repositories import StudentSiblingRepository
from tutorias_itsvc.students.services.siblings.controllers import SiblingGetterController
from tutorias_itsvc.students.services.siblings.controllers import SiblingUpdaterController
from tutorias_itsvc.students.services.siblings.controllers import SiblingDeleterController


class SiblingApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request, student_id, sibling_id):
        repository = StudentSiblingRepository()
        serializer = GetterSerializerService(SiblingSerializer)
        response = ResponseService()
        controller = SiblingGetterController(
            repository=repository,
            serializer=serializer,
            response=response,
        )
        response = controller(student_id, sibling_id)
        return response

    def put(self, request, student_id, sibling_id):
        response = ResponseService()
        request = RequestService(request.data, SiblingSerializer)
        controller = SiblingUpdaterController(
            request=request,
            response=response,
        )
        response = controller(student_id, sibling_id)
        return response

    def delete(self, request, student_id, sibling_id):
        response = ResponseService()
        controller = SiblingDeleterController(
            response=response,
        )
        response = controller(student_id, sibling_id)
        return response
