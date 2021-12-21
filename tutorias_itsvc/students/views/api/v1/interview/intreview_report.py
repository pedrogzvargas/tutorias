from datetime import datetime
from django.core.files.storage import FileSystemStorage
from django.http import HttpResponse
from django.template.loader import render_to_string
from tutorias_itsvc.students.models import Student
from tutorias_itsvc.students.models import StudentParent

from weasyprint import HTML

def html_to_pdf_view(request):
    student = Student.objects.get(id=1)
    father = StudentParent.objects.get(student_id=1, type="father")
    mother = StudentParent.objects.get(student_id=1, type="mother")
    siblings = student.siblings.all()
    academic_information = student.academic.first()
    disabilities = student.disabilities.all()
    date = datetime.now().date()
    html_string = render_to_string('interview/interview.html', {
        'student': student,
        'father': father,
        'mother': mother,
        'date': date,
        'siblings': siblings,
        'academic_information': academic_information,
        'disabilities': disabilities,
    }
    )

    html = HTML(string=html_string, base_url=request.build_absolute_uri())
    html.write_pdf(target='/tmp/mypdf.pdf')

    fs = FileSystemStorage('/tmp')
    with fs.open('mypdf.pdf') as pdf:
        response = HttpResponse(pdf, content_type='application/pdf')
        response['Content-Disposition'] = 'attachment; filename="mypdf.pdf"'
        return response
