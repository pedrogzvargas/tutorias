from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.repositories import StudentIncomeRepository
from tutorias_itsvc.students.serializers.api.v1.income import IncomeSerializer
from tutorias_itsvc.students.services.income.controllers import IncomeGetterController
from tutorias_itsvc.students.services.income.controllers import IncomeCreatorController
from tutorias_itsvc.students.services.income.controllers import IncomeUpdaterController
from tutorias_itsvc.students.services.income.controllers import IncomeDeleterController
from tutorias_itsvc.custom_permission import StudentRecordOwner
from tutorias_itsvc.custom_permission import IsTutor
from tutorias_itsvc.custom_permission import IsAdmin


class IncomeApi(APIView):
    permission_classes = [IsAuthenticated, StudentRecordOwner | IsTutor | IsAdmin]

    def get(self, request, student_id):
        repository = StudentIncomeRepository()
        serializer = GetterSerializerService(IncomeSerializer)
        response = ResponseService()
        getter_controller = IncomeGetterController(
            repository=repository,
            serializer=serializer,
            response=response
        )
        response = getter_controller(student_id=student_id)
        return response

    def post(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, IncomeSerializer)
        controller = IncomeCreatorController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def put(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, IncomeSerializer)
        controller = IncomeUpdaterController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def delete(self, request, student_id):
        response = ResponseService()
        deleter_controller = IncomeDeleterController(
            response=response
        )
        response = deleter_controller(student_id=student_id)
        return response
