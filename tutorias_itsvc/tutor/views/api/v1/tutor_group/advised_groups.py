from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.responses import ResponseService
from shared.requests import RequestService
from shared.serializers import GetterSerializerService
from tutorias_itsvc.academy.repositories import AcademicGroupRepository
from tutorias_itsvc.tutor.serializers.api.v1.tutor_group import TutorGroupCreatorSerializer
from tutorias_itsvc.tutor.serializers.api.v1.tutor_group import TutorGroupSerializer
from tutorias_itsvc.tutor.repositories import TutorGroupRepository
from tutorias_itsvc.tutor.services.tutor_group.controllers import TutorGroupCreatorController
from tutorias_itsvc.tutor.services.tutor_group.controllers import TutorGroupFilterController
from tutorias_itsvc.custom_permission import IsTutor
from tutorias_itsvc.custom_permission import IsAdmin


class AdvisedGroupsApi(APIView):
    permission_classes = [IsAuthenticated, IsTutor | IsAdmin]

    def post(self, request):
        tutor_group_repository = TutorGroupRepository()
        academic_group_repository = AcademicGroupRepository()
        response = ResponseService()
        request = RequestService(request.data, TutorGroupCreatorSerializer)
        controller = TutorGroupCreatorController(
            tutor_group_repository=tutor_group_repository,
            academic_group_repository=academic_group_repository,
            request=request,
            response=response,
        )
        response = controller()
        return response

    def get(self, request):
        repository = TutorGroupRepository()
        serializer = GetterSerializerService(TutorGroupSerializer, True)
        response = ResponseService()
        getter_controller = TutorGroupFilterController(
            request=request,
            repository=repository,
            serializer=serializer,
            response=response
        )
        response = getter_controller()
        return response
