from tutorias_itsvc.students.repositories import StudentIncomeRepository


class IncomeGetterService:
    def __init__(self, repository: StudentIncomeRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
