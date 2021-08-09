from tutorias_itsvc.common.repositories import GenderRepository


class GenderGetterService:
    def __init__(self, repository: GenderRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
