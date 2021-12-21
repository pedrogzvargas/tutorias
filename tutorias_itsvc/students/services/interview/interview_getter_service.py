from tutorias_itsvc.students.repositories import StudentRepository
from django.template.loader import render_to_string
from weasyprint import HTML
import base64


class InterviewGetterService:
    def __init__(self, request, repository: StudentRepository):
        self.__request = request
        self.__repository = repository

    def __call__(self, **kwargs):
        student = self.__repository.get(**kwargs)
        if not student:
            raise Exception("No existe el usuario")
        html_string = render_to_string('interview/interview.html', {"student": student})
        html_as_bytes = HTML(string=html_string, base_url=self.__request.build_absolute_uri()).write_pdf()
        encoded = base64.b64encode(html_as_bytes)
        encoded = encoded.decode('utf-8')
        return dict(file=encoded)
