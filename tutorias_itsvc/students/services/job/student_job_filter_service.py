from tutorias_itsvc.students.repositories import StudentJobRepository


class StudentJobFilterService:
    def __init__(self, repository: StudentJobRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.filter(**kwargs)
