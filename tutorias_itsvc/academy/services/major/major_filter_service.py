from tutorias_itsvc.academy.repositories import MajorRepository


class MajorFilterService:
    def __init__(self, repository: MajorRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.filter(**kwargs)
