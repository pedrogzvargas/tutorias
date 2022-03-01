from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.serializers.api.v1.estilo_aprendizaje import EstiloAprendizajeSerializer
from tutorias_itsvc.students.services.estilo_aprendizaje.controllers import EstiloAprendizajeGetterController
from tutorias_itsvc.students.services.estilo_aprendizaje.controllers import EstiloAprendizajeCreatorController
from tutorias_itsvc.students.services.estilo_aprendizaje.controllers import EstiloAprendizajeUpdaterController
from tutorias_itsvc.students.services.estilo_aprendizaje.controllers import EstiloAprendizajeDeleterController
from tutorias_itsvc.custom_permission import StudentRecordOwner
from tutorias_itsvc.custom_permission import IsTutor
from tutorias_itsvc.custom_permission import IsAdmin


class EstiloAprendizajeApi(APIView):
    permission_classes = [IsAuthenticated, StudentRecordOwner | IsTutor | IsAdmin]

    def get(self, request, student_id):
        serializer = GetterSerializerService(EstiloAprendizajeSerializer)
        response = ResponseService()
        getter_controller = EstiloAprendizajeGetterController(
            serializer=serializer,
            response=response
        )
        response = getter_controller(student_id=student_id)
        return response

    def post(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, EstiloAprendizajeSerializer)
        controller = EstiloAprendizajeCreatorController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def put(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, EstiloAprendizajeSerializer)
        controller = EstiloAprendizajeUpdaterController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def delete(self, request, student_id):
        response = ResponseService()
        deleter_controller = EstiloAprendizajeDeleterController(
            response=response
        )
        response = deleter_controller(student_id=student_id)
        return response
