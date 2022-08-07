from tutorias_itsvc.students.repositories import StudentIncomeRepository
from tutorias_itsvc.students.services.income.exceptions import IncomeNotExist


class IncomeDeleterService:
    def __init__(self, student_income_repository: StudentIncomeRepository):
        self.__student_income_repository = student_income_repository

    def __call__(self, student_id):
        student_income = self.__student_income_repository.get(student_id=student_id)
        if not student_income:
            raise IncomeNotExist(f"No existe un ingreso del usuario con el id {student_id}")
        return self.__student_income_repository.delete(id=student_income.id)
