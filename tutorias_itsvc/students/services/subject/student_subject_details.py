from tutorias_itsvc.students.services.subject import SubjectDetailsService


class StudentSubjectDetailsService:
    def __init__(self,
                 student_repository=None,
                 academic_subject_repository=None,
                 student_subject_repository=None,
                 academic_information_repository=None):

        self.__student_repository = student_repository
        self.__academic_subject_repository = academic_subject_repository
        self.__student_subject_repository = student_subject_repository
        self.__academic_information_repository = academic_information_repository

    def __call__(self, student_id):
        student = self.__student_repository.get(id=student_id)
        if not student:
            raise Exception("No existe el usuario")
        subject_details = SubjectDetailsService(
            student_repository=self.__student_repository,
            academic_subject_repository=self.__academic_subject_repository,
            student_subject_repository=self.__student_subject_repository,
            academic_information_repository=self.__academic_information_repository
        )
        academic_information = self.__academic_information_repository.get(student_id=student_id, is_active=True)
        data = dict(
            student=student,
            subject_details=subject_details(student_id=student_id),
            academic_information=academic_information
        )
        return data
