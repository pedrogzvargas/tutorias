from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.serializers.api.v1.estado_psicofisiologico import EstadoPsicofisiologicoSerializer
from tutorias_itsvc.students.services.estado_psicofisiologico.controllers import EstadoPsicofisiologicoGetterController
from tutorias_itsvc.students.services.estado_psicofisiologico.controllers import EstadoPsicofisiologicoCreatorController
from tutorias_itsvc.students.services.estado_psicofisiologico.controllers import EstadoPsicofisiologicoUpdaterController
from tutorias_itsvc.students.services.estado_psicofisiologico.controllers import EstadoPsicofisiologicoDeleterController


class EstadoPsicofisiologicoApi(APIView):
    permission_classes = ()

    def get(self, request, student_id):
        serializer = GetterSerializerService(EstadoPsicofisiologicoSerializer)
        response = ResponseService()
        getter_controller = EstadoPsicofisiologicoGetterController(
            serializer=serializer,
            response=response
        )
        response = getter_controller(student_id=student_id)
        return response

    def post(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, EstadoPsicofisiologicoSerializer)
        controller = EstadoPsicofisiologicoCreatorController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def put(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, EstadoPsicofisiologicoSerializer)
        controller = EstadoPsicofisiologicoUpdaterController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def delete(self, request, student_id):
        response = ResponseService()
        deleter_controller = EstadoPsicofisiologicoDeleterController(
            response=response
        )
        response = deleter_controller(student_id=student_id)
        return response
