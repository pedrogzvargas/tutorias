from tutorias_itsvc.students.repositories import StudentIncomeRepository


class IncomeUpdaterService:
    def __init__(self, repository: StudentIncomeRepository):
        self.__repository = repository

    def __call__(self, id, **kwargs):
        return self.__repository.update(id, **kwargs)
