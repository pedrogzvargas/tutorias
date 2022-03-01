from rest_framework.views import APIView
from shared.serializers import GetterSerializerService
from shared.responses import ResponseService
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.repositories import OrganizacionEstudioRepository
from tutorias_itsvc.students.repositories import TecnicaEstudioRepository
from tutorias_itsvc.students.repositories import MotivacionEstudioRepository
from tutorias_itsvc.students.repositories import EstiloAprendizajeRepository
from tutorias_itsvc.students.serializers.api.v1.interview import InterviewSerializer
from tutorias_itsvc.students.services.interview_evaluation.controllers import InterviewEvaluationGetterController


class InterviewEvaluationApi(APIView):
    permission_classes = ()

    def get(self, request, student_id):
        student_repository = StudentRepository()
        organizacion_estudio_repository = OrganizacionEstudioRepository()
        tecnica_estudio_repository = TecnicaEstudioRepository()
        motivacion_estudio_repository = MotivacionEstudioRepository()
        estilo_aprendizaje_repository = EstiloAprendizajeRepository()
        serializer = GetterSerializerService(InterviewSerializer)
        response = ResponseService()
        getter_controller = InterviewEvaluationGetterController(
            request=request,
            student_repository=student_repository,
            organizacion_estudio_repository=organizacion_estudio_repository,
            tecnica_estudio_repository=tecnica_estudio_repository,
            motivacion_estudio_repository=motivacion_estudio_repository,
            estilo_aprendizaje_repository=estilo_aprendizaje_repository,
            serializer=serializer,
            response=response
        )
        response = getter_controller(student_id=student_id)
        return response
