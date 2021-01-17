from tutorias_itsvc.academy.repositories import UniversityRepository


class UniversityFilterService:
    def __init__(self, repository: UniversityRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.filter(**kwargs)
