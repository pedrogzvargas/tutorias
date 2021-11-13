from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.serializers.api.v1.scholarship import ScholarshipSerializer
from tutorias_itsvc.students.services.scholarship.controllers import StudentScholarshipGetterController
from tutorias_itsvc.students.services.scholarship.controllers import StudentScholarshipCreatorController
from tutorias_itsvc.students.services.scholarship.controllers import StudentScholarshipUpdaterController
from tutorias_itsvc.students.services.scholarship.controllers import StudentScholarshipDeleterController


class ScholarshipApi(APIView):
    permission_classes = ()

    def get(self, request, student_id):
        serializer = GetterSerializerService(ScholarshipSerializer)
        response = ResponseService()
        getter_controller = StudentScholarshipGetterController(
            serializer=serializer,
            response=response
        )
        response = getter_controller(student_id=student_id)
        return response

    def post(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, ScholarshipSerializer)
        controller = StudentScholarshipCreatorController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def put(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, ScholarshipSerializer)
        controller = StudentScholarshipUpdaterController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def delete(self, request, student_id):
        response = ResponseService()
        deleter_controller = StudentScholarshipDeleterController(
            response=response
        )
        response = deleter_controller(student_id=student_id)
        return response
