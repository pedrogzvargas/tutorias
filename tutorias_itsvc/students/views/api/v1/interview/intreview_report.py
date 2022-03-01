from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.db.models import Count, Case, When
from django.http import HttpResponse
from django.template.loader import render_to_string
from tutorias_itsvc.students.models import Student
from tutorias_itsvc.students.models import OrganizacionEstudio
from tutorias_itsvc.students.models import TecnicaEstudio
from tutorias_itsvc.students.models import MotivacionEstudio
from tutorias_itsvc.students.models import EstiloAprendizaje
from tutorias_itsvc.students.services.interview_evaluation import ResultInterpretation

from weasyprint import HTML

def html_to_pdf_view(request):
    student = Student.objects.get(id=1)

    organizacion = OrganizacionEstudio.objects.filter(student_id=1)
    organizacion_values_as_list = organizacion.values_list()
    organizacion_count = sum(list(organizacion_values_as_list[0])[2:])

    tecnica_estudio = TecnicaEstudio.objects.filter(student_id=1)
    tecnica_estudio_values_as_list = tecnica_estudio.values_list()
    tecnica_estudio_count = sum(list(tecnica_estudio_values_as_list[0])[2:])

    motivacion_estudio = MotivacionEstudio.objects.filter(student_id=1)
    motivacion_estudio_values_as_list = motivacion_estudio.values_list()
    motivacion_estudio_count = sum(list(motivacion_estudio_values_as_list[0])[2:])

    total = organizacion_count + tecnica_estudio_count + motivacion_estudio_count
    results_interpeter = ResultInterpretation(total)
    evaluation = results_interpeter()

    estilo_aprendizaje = EstiloAprendizaje.objects.get(student_id=1)

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

    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    html.write_pdf(target='/tmp/mypdf.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        return response
