from datetime import datetime
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.repositories import ParentRepository
from tutorias_itsvc.common.repositories import SchoolCycleRepository
from django.template.loader import render_to_string
from weasyprint import HTML
import base64


class InterviewGetterService:
    def __init__(self, request, student_repository: StudentRepository, parent_repository: ParentRepository, school_cycle_repository: SchoolCycleRepository):
        self.__request = request
        self.__student_repository = student_repository
        self.__parent_repository = parent_repository
        self.__school_cycle_repository = school_cycle_repository

    def __call__(self, **kwargs):
        student = self.__student_repository.get(**kwargs)
        if not student:
            raise Exception("No existe el usuario")
        father = self.__parent_repository.get(student_id=student.id, type="father")
        mother = self.__parent_repository.get(student_id=student.id, type="mother")
        school_cycle = self.__school_cycle_repository.filter(is_active=True).first()
        siblings = student.siblings.all()
        academic_information = student.academic.first()
        disabilities = student.disabilities.all()
        date = datetime.now().date()
        html_string = render_to_string(
            'interview/interview.html', {
                'student': student,
                'father': father,
                'mother': mother,
                'school_cycle': school_cycle,
                'date': date,
                'siblings': siblings,
                'academic_information': academic_information,
                'disabilities': disabilities,
            }
        )
        html_as_bytes = HTML(string=html_string, base_url=self.__request.build_absolute_uri()).write_pdf()
        encoded = base64.b64encode(html_as_bytes)
        encoded = encoded.decode('utf-8')
        return dict(file=encoded)
