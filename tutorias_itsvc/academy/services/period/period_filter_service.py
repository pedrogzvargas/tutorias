from tutorias_itsvc.academy.repositories import PeriodRepository


class PeriodFilterService:
    def __init__(self, repository: PeriodRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.filter(**kwargs)
