from tutorias_itsvc.students.repositories import ParentRepository


class ParentCreatorService:
    def __init__(self, repository: ParentRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.create(**kwargs)
