from tutorias_itsvc.academy.repositories import PeriodNumberRepository


class PeriodNumberFilterService:
    def __init__(self, repository: PeriodNumberRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.filter(**kwargs)
