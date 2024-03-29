from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from shared.responses import ResponseService
from shared.requests import RequestService
from shared.serializers import GetterSerializerService
from tutorias_itsvc.tutor.serializers.api.v1.tutor_subject import TutorSubjectSerializer
from tutorias_itsvc.tutor.repositories import TutorSubjectRepository
from tutorias_itsvc.tutor.services.tutor_subject.controllers import TutorSubjectGetterController
from tutorias_itsvc.tutor.services.tutor_subject.controllers import TutorSubjectUpdaterController
from tutorias_itsvc.tutor.services.tutor_subject.controllers import TutorSubjectDeleterController
from tutorias_itsvc.custom_permission import IsTutor
from tutorias_itsvc.custom_permission import IsAdmin
from tutorias_itsvc.utils import query_debugger


class TaughtSubjectApi(APIView):
    permission_classes = [IsAuthenticated, IsTutor | IsAdmin]

    @query_debugger
    def get(self, request, taught_subject_id):
        repository = TutorSubjectRepository()
        serializer = GetterSerializerService(TutorSubjectSerializer)
        response = ResponseService()
        getter_controller = TutorSubjectGetterController(
            repository=repository,
            serializer=serializer,
            response=response
        )
        response = getter_controller(id=taught_subject_id)
        return response

    def put(self, request, taught_subject_id):
        repository = TutorSubjectRepository()
        response = ResponseService()
        request = RequestService(request.data, TutorSubjectSerializer)
        controller = TutorSubjectUpdaterController(
            repository=repository,
            request=request,
            response=response,
        )
        response = controller(taught_subject_id)
        return response

    def delete(self, request, taught_subject_id):
        repository = TutorSubjectRepository()
        response = ResponseService()
        deleter_controller = TutorSubjectDeleterController(
            repository=repository,
            response=response
        )
        response = deleter_controller(taught_subject_id=taught_subject_id)
        return response
