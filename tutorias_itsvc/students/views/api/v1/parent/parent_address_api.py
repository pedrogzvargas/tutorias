from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.services.parent.controllers import ParentAddressCreatorController
from tutorias_itsvc.students.services.parent.controllers import ParentAddressGetterController
from tutorias_itsvc.students.services.parent.controllers import ParentAddressUpdaterController
from tutorias_itsvc.students.services.parent.controllers import ParentAddressDeleterController
from tutorias_itsvc.common.serializers.api.v1.address import AddressSerializer
from tutorias_itsvc.common.repositories import AddressRepository
from tutorias_itsvc.custom_permission import StudentRecordOwner
from tutorias_itsvc.custom_permission import IsTutor
from tutorias_itsvc.custom_permission import IsAdmin


class ParentAddressApi(APIView):
    permission_classes = [IsAuthenticated, StudentRecordOwner | IsTutor | IsAdmin]

    def get(self, request, student_id, type):
        repository = AddressRepository()
        serializer = GetterSerializerService(AddressSerializer)
        response = ResponseService()
        controller = ParentAddressGetterController(
            repository=repository,
            serializer=serializer,
            response=response,
        )
        response = controller(student_id=student_id, type=type)
        return response

    def post(self, request, student_id, type):
        response = ResponseService()
        request = RequestService(request.data, AddressSerializer)
        controller = ParentAddressCreatorController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id, type=type)
        return response

    def put(self, request, student_id, type):
        response = ResponseService()
        request = RequestService(request.data, AddressSerializer)
        controller = ParentAddressUpdaterController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id, type=type)
        return response

    def delete(self, request, student_id, type):
        response = ResponseService()
        controller = ParentAddressDeleterController(
            response=response,
        )
        response = controller(student_id=student_id, type=type)
        return response
