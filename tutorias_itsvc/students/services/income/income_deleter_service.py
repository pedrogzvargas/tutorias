from tutorias_itsvc.students.repositories import StudentIncomeRepository


class IncomeDeleterService:
    def __init__(self, repository: StudentIncomeRepository):
        self.__repository = repository

    def __call__(self, id):
        return self.__repository.delete(id)
