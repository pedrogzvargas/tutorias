from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.repositories import OrganizacionEstudioRepository
from tutorias_itsvc.students.repositories import TecnicaEstudioRepository
from tutorias_itsvc.students.repositories import MotivacionEstudioRepository
from tutorias_itsvc.students.repositories import EstiloAprendizajeRepository
from django.template.loader import render_to_string
from weasyprint import HTML
import base64
from .results_interpretation import ResultInterpretation


class InterviewEvaluationGetterService:
    def __init__(
        self,
        request,
        student_repository: StudentRepository,
        organizacion_estudio_repository: OrganizacionEstudioRepository,
        tecnica_estudio_repository: TecnicaEstudioRepository,
        motivacion_estudio_repository: MotivacionEstudioRepository,
        estilo_aprendizaje_repository: EstiloAprendizajeRepository,
    ):
        self.__request = request
        self.__student_repository = student_repository
        self.__organizacion_estudio_repository = organizacion_estudio_repository
        self.__tecnica_estudio_repository = tecnica_estudio_repository
        self.__motivacion_estudio_repository = motivacion_estudio_repository
        self.__motivacion_estudio_repository = motivacion_estudio_repository
        self.__estilo_aprendizaje_repository = estilo_aprendizaje_repository

    def __call__(self, student_id):
        student = self.__student_repository.get(id=student_id)
        if not student:
            raise Exception("No existe el usuario")

        organizacion = self.__organizacion_estudio_repository.filter(student_id=student_id)
        organizacion_values_as_list = organizacion.values_list()
        organizacion_count = sum(list(organizacion_values_as_list[0])[2:])

        tecnica_estudio = self.__tecnica_estudio_repository.filter(student_id=student_id)
        tecnica_estudio_values_as_list = tecnica_estudio.values_list()
        tecnica_estudio_count = sum(list(tecnica_estudio_values_as_list[0])[2:])

        motivacion_estudio = self.__motivacion_estudio_repository.filter(student_id=student_id)
        motivacion_estudio_values_as_list = motivacion_estudio.values_list()
        motivacion_estudio_count = sum(list(motivacion_estudio_values_as_list[0])[2:])

        total = organizacion_count + tecnica_estudio_count + motivacion_estudio_count
        results_interpeter = ResultInterpretation(total)
        evaluation = results_interpeter()

        estilo_aprendizaje = self.__estilo_aprendizaje_repository.get(student_id=student_id)

        total_visual = (
            estilo_aprendizaje.p1 + estilo_aprendizaje.p3 +
            estilo_aprendizaje.p6 + estilo_aprendizaje.p9 +
            estilo_aprendizaje.p10 + estilo_aprendizaje.p11 +
            estilo_aprendizaje.p14
        )

        total_auditivo = (
            estilo_aprendizaje.p2 + estilo_aprendizaje.p5 +
            estilo_aprendizaje.p12 + estilo_aprendizaje.p15 +
            estilo_aprendizaje.p17 + estilo_aprendizaje.p21 +
            estilo_aprendizaje.p23
        )

        total_kinestesico = (
            estilo_aprendizaje.p4 + estilo_aprendizaje.p7 +
            estilo_aprendizaje.p8 + estilo_aprendizaje.p13 +
            estilo_aprendizaje.p19 + estilo_aprendizaje.p22 +
            estilo_aprendizaje.p24
        )

        html_string = render_to_string('interview/interview_evaluation.html', {
            'student': student,
            'organizacion_count': organizacion_count,
            'tecnica_estudio_count': tecnica_estudio_count,
            'motivacion_estudio_count': motivacion_estudio_count,
            'estilo_aprendizaje': estilo_aprendizaje,
            'total_visual': total_visual,
            'total_auditivo': total_auditivo,
            'total_kinestesico': total_kinestesico,
            'total': total,
            'evaluation': evaluation,
        }
                                       )
        html_as_bytes = HTML(string=html_string, base_url=self.__request.build_absolute_uri()).write_pdf()
        encoded = base64.b64encode(html_as_bytes)
        encoded = encoded.decode('utf-8')
        return dict(file=encoded)
