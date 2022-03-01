from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.serializers.api.v1.motivacion_estudio import MotivacionEstudioSerializer
from tutorias_itsvc.students.services.motivacion_estudio.controllers import MotivacionEstudioGetterController
from tutorias_itsvc.students.services.motivacion_estudio.controllers import MotivacionEstudioCreatorController
from tutorias_itsvc.students.services.motivacion_estudio.controllers import MotivacionEstudioUpdaterController
from tutorias_itsvc.students.services.motivacion_estudio.controllers import MotivacionEstudioDeleterController
from tutorias_itsvc.custom_permission import StudentRecordOwner
from tutorias_itsvc.custom_permission import IsTutor
from tutorias_itsvc.custom_permission import IsAdmin


class MotivacionEstudioApi(APIView):
    permission_classes = [IsAuthenticated, StudentRecordOwner | IsTutor | IsAdmin]

    def get(self, request, student_id):
        serializer = GetterSerializerService(MotivacionEstudioSerializer)
        response = ResponseService()
        getter_controller = MotivacionEstudioGetterController(
            serializer=serializer,
            response=response
        )
        response = getter_controller(student_id=student_id)
        return response

    def post(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, MotivacionEstudioSerializer)
        controller = MotivacionEstudioCreatorController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def put(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, MotivacionEstudioSerializer)
        controller = MotivacionEstudioUpdaterController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def delete(self, request, student_id):
        response = ResponseService()
        deleter_controller = MotivacionEstudioDeleterController(
            response=response
        )
        response = deleter_controller(student_id=student_id)
        return response
