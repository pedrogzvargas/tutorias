from tutorias_itsvc.students.repositories import StudentRepository


class StudentCreatorService:
    def __init__(self, repository: StudentRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.create(**kwargs)
