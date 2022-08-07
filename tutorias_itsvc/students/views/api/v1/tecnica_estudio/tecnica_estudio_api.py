from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.serializers.api.v1.tecnica_estudio import TecnicaEstudioSerializer
from tutorias_itsvc.students.services.tecnica_estudio.controllers import TecnicaEstudioGetterController
from tutorias_itsvc.students.services.tecnica_estudio.controllers import TecnicaEstudioCreatorController
from tutorias_itsvc.students.services.tecnica_estudio.controllers import TecnicaEstudioUpdaterController
from tutorias_itsvc.students.services.tecnica_estudio.controllers import TecnicaEstudioDeleterController
from tutorias_itsvc.custom_permission import StudentRecordOwner
from tutorias_itsvc.custom_permission import IsTutor
from tutorias_itsvc.custom_permission import IsAdmin


class TecnicaEstudioApi(APIView):
    permission_classes = [IsAuthenticated, StudentRecordOwner | IsTutor | IsAdmin]

    def get(self, request, student_id):
        serializer = GetterSerializerService(TecnicaEstudioSerializer)
        response = ResponseService()
        getter_controller = TecnicaEstudioGetterController(
            serializer=serializer,
            response=response
        )
        response = getter_controller(student_id=student_id)
        return response

    def post(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, TecnicaEstudioSerializer)
        controller = TecnicaEstudioCreatorController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def put(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, TecnicaEstudioSerializer)
        controller = TecnicaEstudioUpdaterController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def delete(self, request, student_id):
        response = ResponseService()
        deleter_controller = TecnicaEstudioDeleterController(
            response=response
        )
        response = deleter_controller(student_id=student_id)
        return response
