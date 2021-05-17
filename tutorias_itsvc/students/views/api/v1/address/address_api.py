from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.repositories import AddressRepository
from tutorias_itsvc.students.serializers.api.v1.address import AddressSerializer
from tutorias_itsvc.students.services.address.controllers import AddressGetterController
from tutorias_itsvc.students.services.address.controllers import AddressCreatorController
from tutorias_itsvc.students.services.address.controllers import AddressUpdaterController
from tutorias_itsvc.students.services.address.controllers import AddressDeleterController


class AddressApi(APIView):
    permission_classes = ()

    def get(self, request, student_id):
        repository = AddressRepository()
        serializer = GetterSerializerService(AddressSerializer)
        response = ResponseService()
        getter_controller = AddressGetterController(
            repository=repository,
            serializer=serializer,
            response=response
        )
        response = getter_controller(student_id=student_id)
        return response

    def post(self, request, student_id):
        repository = AddressRepository()
        response = ResponseService()
        request = RequestService(request.data, AddressSerializer)
        creator_controller = AddressCreatorController(
            request=request,
            repository=repository,
            response=response,
        )
        response = creator_controller(student_id=student_id)
        return response

    def put(self, request, student_id):
        repository = AddressRepository()
        response = ResponseService()
        request = RequestService(request.data, AddressSerializer)
        updater_controller = AddressUpdaterController(
            request=request,
            repository=repository,
            response=response,
        )
        response = updater_controller(student_id=student_id)
        return response

    def delete(self, request, student_id):
        repository = AddressRepository()
        response = ResponseService()
        deleter_controller = AddressDeleterController(
            repository=repository,
            response=response,
        )
        response = deleter_controller(student_id=student_id)
        return response
