from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from tutorias_itsvc.users.repositories import ProfileImageRepository
from tutorias_itsvc.users.serializers.api.v1.profile_image import ProfileImageSerializer
from tutorias_itsvc.users.services.profile_image.controllers import ProfileImageGetterController


class ProfileImageApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request, user_id):
        repository = ProfileImageRepository()
        serializer = GetterSerializerService(ProfileImageSerializer, context={"request": request})
        response = ResponseService()
        controller = ProfileImageGetterController(
            repository=repository,
            serializer=serializer,
            response=response,
        )
        response = controller(user_id=user_id)
        return response
