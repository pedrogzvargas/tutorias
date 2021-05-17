from tutorias_itsvc.students.repositories import ParentRepository


class ParentDeleterService:
    def __init__(self, repository: ParentRepository):
        self.__repository = repository

    def __call__(self, id):
        return self.__repository.delete(id)
