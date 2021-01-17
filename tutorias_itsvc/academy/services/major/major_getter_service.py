from tutorias_itsvc.academy.repositories import MajorRepository


class MajorGetterService:
    def __init__(self, repository: MajorRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
