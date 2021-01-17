from tutorias_itsvc.academy.repositories import UniversityRepository


class UniversityGetterService:
    def __init__(self, repository: UniversityRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
