from tutorias_itsvc.common.repositories import GenderRepository


class GenderFilterService:
    def __init__(self, repository: GenderRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.filter(**kwargs)
