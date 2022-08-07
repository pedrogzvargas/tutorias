from tutorias_itsvc.students.repositories import StudentIncomeRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.services.student.exceptions import StudentNotExist


class IncomeCreatorService:
    def __init__(self, student_income_repository: StudentIncomeRepository, student_repository: StudentRepository):
        self.__student_income_repository = student_income_repository
        self.__student_repository = student_repository

    def __call__(self, student_id, income=None, family_income=None):
        student = self.__student_repository.get(id=student_id)
        if not student:
            raise StudentNotExist(f"No existe un estudiante con el id {student_id}")
        return self.__student_income_repository.create(student_id=student_id,
                                                       income=income,
                                                       family_income=family_income)
