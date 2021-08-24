from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.responses import ResponseService
from shared.requests import RequestService
from shared.serializers import GetterSerializerService
from tutorias_itsvc.academy.repositories import AcademicGroupRepository
from tutorias_itsvc.tutor.serializers.api.v1.tutor_group import TutorGroupUpdaterSerializer
from tutorias_itsvc.tutor.serializers.api.v1.tutor_group import TutorGroupSerializer
from tutorias_itsvc.tutor.repositories import TutorGroupRepository
from tutorias_itsvc.tutor.services.tutor_group.controllers import TutorGroupUpdaterController
from tutorias_itsvc.tutor.services.tutor_group.controllers import TutorGroupGetterController
from tutorias_itsvc.tutor.services.tutor_group.controllers import TutorGroupDeleterController


class AdvisedGroupApi(APIView):
    permission_classes = (IsAuthenticated, )

    def get(self, request, advised_group_id):
        repository = TutorGroupRepository()
        serializer = GetterSerializerService(TutorGroupSerializer)
        response = ResponseService()
        getter_controller = TutorGroupGetterController(
            repository=repository,
            serializer=serializer,
            response=response
        )
        response = getter_controller(id=advised_group_id)
        return response

    def put(self, request, advised_group_id):
        tutor_group_repository = TutorGroupRepository()
        academic_group_repository = AcademicGroupRepository()
        response = ResponseService()
        request = RequestService(request.data, TutorGroupUpdaterSerializer)
        controller = TutorGroupUpdaterController(
            tutor_group_repository=tutor_group_repository,
            academic_group_repository=academic_group_repository,
            request=request,
            response=response,
        )
        response = controller(advised_group_id=advised_group_id)
        return response

    def delete(self, request, advised_group_id):
        repository = TutorGroupRepository()
        response = ResponseService()
        getter_controller = TutorGroupDeleterController(
            repository=repository,
            response=response
        )
        response = getter_controller(advised_group_id=advised_group_id)
        return response
