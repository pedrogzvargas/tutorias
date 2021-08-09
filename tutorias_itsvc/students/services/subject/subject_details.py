from django.db.models import Sum
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.repositories import StudentSubjectRepository
from tutorias_itsvc.students.services.student import StudentGetterService
from tutorias_itsvc.students.services.subject import StudentSubjectFilterService
from tutorias_itsvc.academy.repositories import AcademicSubjectRepository
from tutorias_itsvc.academy.services.academic_subject import AcademicSubjectFilterService
from tutorias_itsvc.students.services.academic_information import AcademicInformationGetterService
from tutorias_itsvc.students.repositories import AcademicInformationRepository


class SubjectDetailsService:
    def __init__(self, student_id):
        self.__student_id = student_id

    def get_academic_information(self):
        repository = AcademicInformationRepository()
        getter_service = AcademicInformationGetterService(repository)
        academic_information = getter_service(student_id=self.__student_id, is_active=True)
        return academic_information

    def get_subjects(self, major_id):
        repository = AcademicSubjectRepository()
        filter_service = AcademicSubjectFilterService(repository)
        subjects = filter_service(academic_period_number__academic_period__academic_major__major_id=major_id)
        return subjects

    def get_student(self):
        repository = StudentRepository()
        getter_service = StudentGetterService(repository)
        student = getter_service(id=self.__student_id)
        return student

    def get_taking_subjects(self):
        repository = StudentSubjectRepository()
        filter_service = StudentSubjectFilterService(repository)
        takinng_subjects = filter_service(student_id=self.__student_id, approved__isnull=True, unsubscribed=False)
        return takinng_subjects

    def get_taking_subjects_points(self, taking_subjects):
        taking_subjects_sum = taking_subjects.aggregate(
            Sum('subject__total_value')
        ).get('subject__total_value__sum') or 0
        return taking_subjects_sum

    def get_approved_subjects(self):
        repository = StudentSubjectRepository()
        filter_service = StudentSubjectFilterService(repository)
        approved_subjects = filter_service(student_id=self.__student_id, approved=True)
        return approved_subjects

    def get_approved_subjects_points(self, approved_subjects):
        approved_subjects_sum = approved_subjects.aggregate(
            Sum('subject__total_value')
        ).get('subject__total_value__sum') or 0
        return approved_subjects_sum

    def get_failed_subjects(self):
        repository = StudentSubjectRepository()
        filter_service = StudentSubjectFilterService(repository)
        approved_subjects = filter_service(student_id=self.__student_id, approved=False)
        return approved_subjects

    def __call__(self):
        student = self.get_student()
        if not student:
            raise Exception('Usuario no encontrado')
        academic_information = self.get_academic_information()
        major_id = academic_information.academic_information.academic_period_number.academic_period.academic_major.major.id
        subjects = self.get_subjects(major_id)
        taking_subjects = self.get_taking_subjects()
        approved_subjects = self.get_approved_subjects()
        failed_subjects = self.get_failed_subjects()
        approved_subjects_points = self.get_approved_subjects_points(approved_subjects)
        taking_subjects_points = self.get_taking_subjects_points(taking_subjects)
        subject_details = dict(
            subjects=subjects.count(),
            taking_subjects=taking_subjects.count(),
            approved_subjects=approved_subjects.count(),
            failed_subjects=failed_subjects.count(),
            approved_subjects_points=approved_subjects_points,
            taking_subjects_points=taking_subjects_points,
            total_points=approved_subjects_points + taking_subjects_points
        )
        return subject_details
