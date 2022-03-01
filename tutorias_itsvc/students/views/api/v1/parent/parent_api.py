from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.repositories import ParentRepository
from tutorias_itsvc.students.services.parent.controllers import ParentGetterController
from tutorias_itsvc.students.services.parent.controllers import ParentCreatorController
from tutorias_itsvc.students.services.parent.controllers import ParentUpdaterController
from tutorias_itsvc.students.services.parent.controllers import ParentDeleterController
from tutorias_itsvc.students.serializers.api.v1.parent import ParentSerializer
from tutorias_itsvc.custom_permission import StudentRecordOwner
from tutorias_itsvc.custom_permission import IsTutor
from tutorias_itsvc.custom_permission import IsAdmin


class ParentApi(APIView):
    permission_classes = [IsAuthenticated, StudentRecordOwner | IsTutor | IsAdmin]

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
        response = ResponseService()
        request = RequestService(request.data, ParentSerializer)
        controller = ParentCreatorController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id, type=type)
        return response

    def put(self, request, student_id, type):
        response = ResponseService()
        request = RequestService(request.data, ParentSerializer)
        controller = ParentUpdaterController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id, type=type)
        return response

    def delete(self, request, student_id, type):
        response = ResponseService()
        controller = ParentDeleterController(
            response=response,
        )
        response = controller(student_id=student_id, type=type)
        return response
