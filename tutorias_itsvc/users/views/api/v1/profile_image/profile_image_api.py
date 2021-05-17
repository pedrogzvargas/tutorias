from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.users.repositories import ProfileImageRepository
from tutorias_itsvc.users.serializers.api.v1.profile_image import ProfileImageSerializer
from tutorias_itsvc.users.serializers.api.v1.profile_image import UploadProfileImage
from tutorias_itsvc.users.services.profile_image.controllers import ProfileImageGetterController
from tutorias_itsvc.users.services.profile_image.controllers import ProfileImageCreatorController


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

    def post(self, request, user_id):
        repository = ProfileImageRepository()
        request = RequestService(request.data, UploadProfileImage)
        response = ResponseService()
        controller = ProfileImageCreatorController(
            repository=repository,
            request=request,
            response=response,
        )
        response = controller(user_id=user_id)
        return response
