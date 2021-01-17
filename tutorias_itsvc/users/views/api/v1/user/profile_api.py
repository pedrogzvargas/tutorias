from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.users.repositories import UserRepository
from tutorias_itsvc.users.serializers.api.v1.user import ProfileSerializer
from tutorias_itsvc.users.services.user.controllers import UserGetterController, UserSetterController


class ProfileApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request, user_id):
        repository = UserRepository()
        serializer = GetterSerializerService(ProfileSerializer)
        response = ResponseService()
        controller = UserGetterController(
            repository=repository,
            serializer=serializer,
            response=response,
        )
        response = controller(id=user_id)
        return response

    def put(self, request, user_id):
        repository = UserRepository()
        response = ResponseService()
        request = RequestService(request.data, ProfileSerializer)
        controller = UserSetterController(
            request=request,
            repository=repository,
            response=response,
        )
        response = controller(user_id=user_id)
        return response
