from tutorias_itsvc.students.repositories import StudentIncomeRepository


class IncomeCreatorService:
    def __init__(self, repository: StudentIncomeRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.create(**kwargs)
