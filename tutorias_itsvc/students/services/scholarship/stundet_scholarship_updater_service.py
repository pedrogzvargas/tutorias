from tutorias_itsvc.students.repositories import StudentScholarshipRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.services.student.exceptions import StudentNotExist
from tutorias_itsvc.students.services.scholarship.exceptions import ScholarshipAlreadyExist


class StudentScholarshipUpdaterService:
    def __init__(self,
                 student_scholarship_repository: StudentScholarshipRepository,
                 student_repository: StudentRepository):
        self.__student_scholarship_repository = student_scholarship_repository
        self.__student_repository = student_repository

    def __call__(self, student_id, has_scholarship, institute_name, dependence_name):
        student_scholarship = self.__student_scholarship_repository.get(student_id=student_id)
        if not student_scholarship:
            raise ScholarshipAlreadyExist(f"No existe un registro de beca para el usuario con id {student_id}")
        student = self.__student_repository.get(id=student_id)
        if not student:
            raise StudentNotExist(f"No existe estudiante con id {student_id}")
        return self.__student_scholarship_repository.update(
            id=student_scholarship.id,
            student_id=student_id,
            has_scholarship=has_scholarship,
            institute_name=institute_name,
            dependence_name=dependence_name
        )
