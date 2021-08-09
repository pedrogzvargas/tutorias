from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
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


class TutorGroupApi(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, tutor_group_id):
        repository = TutorGroupRepository()
        serializer = GetterSerializerService(TutorGroupSerializer)
        response = ResponseService()
        getter_controller = TutorGroupGetterController(
            repository=repository,
            serializer=serializer,
            response=response
        )
        response = getter_controller(id=tutor_group_id)
        return response

    def put(self, request, tutor_group_id):
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
        response = controller(tutor_group_id=tutor_group_id)
        return response

    def delete(self, request, tutor_group_id):
        repository = TutorGroupRepository()
        response = ResponseService()
        getter_controller = TutorGroupDeleterController(
            repository=repository,
            response=response
        )
        response = getter_controller(tutor_group_id=tutor_group_id)
        return response
