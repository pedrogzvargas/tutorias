from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.responses import ResponseService
from shared.requests import RequestService

from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.users.repositories import UserRepository
from tutorias_itsvc.users.repositories import GroupRepository
from tutorias_itsvc.students.serializers.api.v1.load_data import StudentsLoadDataSerializer
from tutorias_itsvc.students.services.load_data.controllers import StudentsLoaderController
from tutorias_itsvc.custom_permission import IsTutor
from tutorias_itsvc.custom_permission import IsAdmin


class StudentsLoadDataApi(APIView):
    permission_classes = [IsAuthenticated, IsTutor | IsAdmin]

    def post(self, request):
        student_repository = StudentRepository()
        user_repository = UserRepository()
        group_repository = GroupRepository()
        response = ResponseService()
        request = RequestService(request.data, StudentsLoadDataSerializer)
        controller = StudentsLoaderController(
            student_repository=student_repository,
            user_repository=user_repository,
            group_repository=group_repository,
            request=request,
            response=response,
        )
        response = controller()
        return response
