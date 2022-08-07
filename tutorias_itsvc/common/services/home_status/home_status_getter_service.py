from tutorias_itsvc.common.repositories import HomeStatusRepository


class HomeStatusGetterService:
    def __init__(self, repository: HomeStatusRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
