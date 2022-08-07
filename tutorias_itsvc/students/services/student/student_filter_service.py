from tutorias_itsvc.students.repositories import StudentRepository


class StudentFilterService:
    def __init__(self, repository: StudentRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.filter(**kwargs)
