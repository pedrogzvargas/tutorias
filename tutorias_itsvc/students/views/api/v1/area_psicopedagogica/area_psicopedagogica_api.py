from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.serializers.api.v1.area_psicopedagogica import AreaPsicopedagogicaSerializer
from tutorias_itsvc.students.services.area_psicopedagogica.controllers import AreaPsicopedagogicaGetterController
from tutorias_itsvc.students.services.area_psicopedagogica.controllers import AreaPsicopedagogicaCreatorController
from tutorias_itsvc.students.services.area_psicopedagogica.controllers import AreaPsicopedagogicaUpdaterController
from tutorias_itsvc.students.services.area_psicopedagogica.controllers import AreaPsicopedagogicaDeleterController


class AreaPsicopedagogicaApi(APIView):
    permission_classes = ()

    def get(self, request, student_id):
        serializer = GetterSerializerService(AreaPsicopedagogicaSerializer)
        response = ResponseService()
        getter_controller = AreaPsicopedagogicaGetterController(
            serializer=serializer,
            response=response
        )
        response = getter_controller(student_id=student_id)
        return response

    def post(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, AreaPsicopedagogicaSerializer)
        controller = AreaPsicopedagogicaCreatorController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def put(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, AreaPsicopedagogicaSerializer)
        controller = AreaPsicopedagogicaUpdaterController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def delete(self, request, student_id):
        response = ResponseService()
        deleter_controller = AreaPsicopedagogicaDeleterController(
            response=response
        )
        response = deleter_controller(student_id=student_id)
        return response
