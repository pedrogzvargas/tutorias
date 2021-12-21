from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.serializers.api.v1.caracterisitcas_personales import CaracteristicasPersonalesSerializer
from tutorias_itsvc.students.services.caracteristicas_personales.controllers import CaracteristicasPersonalesGetterController
from tutorias_itsvc.students.services.caracteristicas_personales.controllers import CaracteristicasPersonalesCreatorController
from tutorias_itsvc.students.services.caracteristicas_personales.controllers import CaracteristicasPersonalesUpdaterController
from tutorias_itsvc.students.services.caracteristicas_personales.controllers import CaracteristicasPersonalesDeleterController


class CaracteristicasPersonalesApi(APIView):
    permission_classes = ()

    def get(self, request, student_id):
        serializer = GetterSerializerService(CaracteristicasPersonalesSerializer)
        response = ResponseService()
        getter_controller = CaracteristicasPersonalesGetterController(
            serializer=serializer,
            response=response
        )
        response = getter_controller(student_id=student_id)
        return response

    def post(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, CaracteristicasPersonalesSerializer)
        controller = CaracteristicasPersonalesCreatorController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def put(self, request, student_id):
        response = ResponseService()
        request = RequestService(request.data, CaracteristicasPersonalesSerializer)
        controller = CaracteristicasPersonalesUpdaterController(
            request=request,
            response=response,
        )
        response = controller(student_id=student_id)
        return response

    def delete(self, request, student_id):
        response = ResponseService()
        deleter_controller = CaracteristicasPersonalesDeleterController(
            response=response
        )
        response = deleter_controller(student_id=student_id)
        return response
