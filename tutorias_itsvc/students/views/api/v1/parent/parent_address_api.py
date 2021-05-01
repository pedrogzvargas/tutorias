from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.services.parent.controllers import ParentGetterController
from tutorias_itsvc.students.services.parent.controllers import ParentAddressCreatorController
from tutorias_itsvc.students.services.parent.controllers import ParentAddressGetterController
from tutorias_itsvc.students.services.parent.controllers import ParentUpdaterController
from tutorias_itsvc.common.serializers.api.v1.address import AddressSerializer
from tutorias_itsvc.common.repositories import AddressRepository


class ParentAddressApi(APIView):
    permission_classes = [AllowAny]

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
        repository = AddressRepository()
        response = ResponseService()
        request = RequestService(request.data, AddressSerializer)
        controller = ParentAddressCreatorController(
            repository=repository,
            request=request,
            response=response,
        )
        response = controller(student_id=student_id, type=type)
        return response

    # def put(self, request, student_id, type):
    #     repository = ParentRepository()
    #     response = ResponseService()
    #     request = RequestService(request.data, ParentSerializer)
    #     controller = ParentUpdaterController(
    #         repository=repository,
    #         request=request,
    #         response=response,
    #     )
    #     response = controller(student_id=student_id, type=type)
    #     return response
