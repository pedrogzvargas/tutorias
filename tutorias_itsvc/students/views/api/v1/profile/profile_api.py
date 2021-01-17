from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from shared.requests import RequestService
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.serializers.api.v1.profile import ProfileSerializer
from tutorias_itsvc.students.services.profile.controllers import ProfileGetterController, ProfileSetterController


class ProfileApi(APIView):
    permission_classes = [AllowAny]

    def get(self, request, student_id):
        repository = StudentRepository()
        serializer = GetterSerializerService(ProfileSerializer)
        response = ResponseService()
        controller = ProfileGetterController(
            repository=repository,
            serializer=serializer,
            response=response,
        )
        response = controller(id=student_id)
        return response

    def put(self, request, student_id):
        repository = StudentRepository()
        response = ResponseService()
        request = RequestService(request.data, ProfileSerializer)
        controller = ProfileSetterController(
            request=request,
            repository=repository,
            response=response,
        )
        response = controller(id=student_id)
        return response
