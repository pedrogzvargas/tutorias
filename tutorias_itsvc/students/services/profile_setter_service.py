from tutorias_itsvc.students.repositories import StudentRepository


class ProfileSetterService:
    def __init__(self, repository: StudentRepository):
        self.__repository = repository

    def __call__(self, id, **kwargs):
        return self.__repository.update(id, **kwargs)
