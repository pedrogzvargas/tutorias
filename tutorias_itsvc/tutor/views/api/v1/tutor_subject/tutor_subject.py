from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from shared.responses import ResponseService
from shared.requests import RequestService
from shared.serializers import GetterSerializerService
from tutorias_itsvc.tutor.serializers.api.v1.tutor_subject import TutorSubjectSerializer
from tutorias_itsvc.tutor.repositories import TutorSubjectRepository
from tutorias_itsvc.tutor.services.tutor_subject.controllers import TutorSubjectGetterController
from tutorias_itsvc.tutor.services.tutor_subject.controllers import TutorSubjectUpdaterController
from tutorias_itsvc.tutor.services.tutor_subject.controllers import TutorSubjectDeleterController


class TutorSubjectApi(APIView):
    permission_classes = (AllowAny, )

    def get(self, request, tutor_subject_id):
        repository = TutorSubjectRepository()
        serializer = GetterSerializerService(TutorSubjectSerializer)
        response = ResponseService()
        getter_controller = TutorSubjectGetterController(
            repository=repository,
            serializer=serializer,
            response=response
        )
        response = getter_controller(id=tutor_subject_id)
        return response

    def put(self, request, tutor_subject_id):
        repository = TutorSubjectRepository()
        response = ResponseService()
        request = RequestService(request.data, TutorSubjectSerializer)
        controller = TutorSubjectUpdaterController(
            repository=repository,
            request=request,
            response=response,
        )
        response = controller(tutor_subject_id)
        return response

    def delete(self, request, tutor_subject_id):
        repository = TutorSubjectRepository()
        response = ResponseService()
        getter_controller = TutorSubjectDeleterController(
            repository=repository,
            response=response
        )
        response = getter_controller(tutor_subject_id=tutor_subject_id)
        return response
