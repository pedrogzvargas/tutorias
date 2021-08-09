from tutorias_itsvc.common.repositories import MaritalStatusRepository


class MaritalStatusGetterService:
    def __init__(self, repository: MaritalStatusRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
