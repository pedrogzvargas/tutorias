from tutorias_itsvc.students.repositories import ParentRepository


class ParentUpdaterService:
    def __init__(self, repository: ParentRepository):
        self.__repository = repository

    def __call__(self, id, **kwargs):
        return self.__repository.update(id, **kwargs)
