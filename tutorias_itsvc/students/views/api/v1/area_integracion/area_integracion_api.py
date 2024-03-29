from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.serializers.api.v1.area_integracion import AreaIntegracionSerializer
from tutorias_itsvc.students.services.area_integracion.controllers import AreaIntegracionGetterController
from tutorias_itsvc.students.services.area_integracion.controllers import AreaIntegracionCreatorController
from tutorias_itsvc.students.services.area_integracion.controllers import AreaIntegracionUpdaterController
from tutorias_itsvc.students.services.area_integracion.controllers import AreaIntegracionDeleterController
from tutorias_itsvc.custom_permission import StudentRecordOwner
from tutorias_itsvc.custom_permission import IsTutor
from tutorias_itsvc.custom_permission import IsAdmin


class AreaIntegracionApi(APIView):
    permission_classes = [IsAuthenticated, StudentRecordOwner | IsTutor | IsAdmin]

    def get(self, request, student_id):
        serializer = GetterSerializerService(AreaIntegracionSerializer)
        response = ResponseService()
        getter_controller = AreaIntegracionGetterController(
            serializer=serializer,
            response=response
        )
        response = getter_controller(student_id=student_id)
        return response

    def post(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, AreaIntegracionSerializer)
        controller = AreaIntegracionCreatorController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def put(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, AreaIntegracionSerializer)
        controller = AreaIntegracionUpdaterController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def delete(self, request, student_id):
        response = ResponseService()
        deleter_controller = AreaIntegracionDeleterController(
            response=response
        )
        response = deleter_controller(student_id=student_id)
        return response
