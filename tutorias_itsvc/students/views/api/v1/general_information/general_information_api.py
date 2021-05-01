from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.services.general_information.controllers import GeneralInformationGetterController
from tutorias_itsvc.students.services.general_information.controllers import GeneralInformationCreatorController
from tutorias_itsvc.students.services.general_information.controllers import GeneralInformationUpdaterController
from tutorias_itsvc.students.serializers.api.v1.general_information import GeneralInformationSerializer
from tutorias_itsvc.utils import query_debugger


class GeneralInformationApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request, user_id):
        serializer = GetterSerializerService(GeneralInformationSerializer)
        response = ResponseService()
        controller = GeneralInformationGetterController(
            serializer=serializer,
            response=response,
        )
        response = controller(user_id=user_id)
        return response

    def post(self, request, user_id):
        response = ResponseService()
        request = RequestService(request.data, GeneralInformationSerializer)
        controller = GeneralInformationCreatorController(
            request=request,
            response=response,
        )
        response = controller(user_id=user_id)
        return response

    def put(self, request, user_id):
        response = ResponseService()
        request = RequestService(request.data, GeneralInformationSerializer)
        controller = GeneralInformationUpdaterController(
            request=request,
            response=response,
        )
        response = controller(user_id=user_id)
        return response
