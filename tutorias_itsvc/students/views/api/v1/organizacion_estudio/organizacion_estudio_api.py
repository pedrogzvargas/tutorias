from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.serializers.api.v1.organizacion_estudio import OrganizacionEstudioSerializer
from tutorias_itsvc.students.services.organizacion_estudio.controllers import OrganizacionEstudioGetterController
from tutorias_itsvc.students.services.organizacion_estudio.controllers import OrganizacionEstudioCreatorController
from tutorias_itsvc.students.services.organizacion_estudio.controllers import OrganizacionEstudioUpdaterController
from tutorias_itsvc.students.services.organizacion_estudio.controllers import OrganizacionEstudioDeleterController


class OrganizacionEstudioApi(APIView):
    permission_classes = ()

    def get(self, request, student_id):
        serializer = GetterSerializerService(OrganizacionEstudioSerializer)
        response = ResponseService()
        getter_controller = OrganizacionEstudioGetterController(
            serializer=serializer,
            response=response
        )
        response = getter_controller(student_id=student_id)
        return response

    def post(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, OrganizacionEstudioSerializer)
        controller = OrganizacionEstudioCreatorController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def put(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, OrganizacionEstudioSerializer)
        controller = OrganizacionEstudioUpdaterController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def delete(self, request, student_id):
        response = ResponseService()
        deleter_controller = OrganizacionEstudioDeleterController(
            response=response
        )
        response = deleter_controller(student_id=student_id)
        return response
