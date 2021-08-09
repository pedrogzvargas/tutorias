from tutorias_itsvc.common.repositories import MaritalStatusRepository


class MaritalStatusFilterService:
    def __init__(self, repository: MaritalStatusRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.filter(**kwargs)
