from tutorias_itsvc.common.repositories import HomeStatusRepository


class HomeStatusFilterService:
    def __init__(self, repository: HomeStatusRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.filter(**kwargs)
