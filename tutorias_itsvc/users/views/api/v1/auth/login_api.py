from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.responses import ResponseService
from shared.requests import RequestService
from shared.serializers import GetterSerializerService
from tutorias_itsvc.users.serializers.api.v1.auth import LoginCreatorSerializer, LoginGetterSerializer
from tutorias_itsvc.users.services.auth.controllers import LoginController


class LoginApi(APIView):
    """
    Login API
    """
    permission_classes = [AllowAny]
    def post(self, request):
        request = RequestService(request.data, LoginCreatorSerializer)
        response = ResponseService()
        serializer = GetterSerializerService(LoginGetterSerializer)
        login_controller = LoginController(
            request=request,
            serializer=serializer,
            response=response
        )
        response = login_controller()
        return response
