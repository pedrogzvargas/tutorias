from tutorias_itsvc.common.repositories import StateRepository


class StateGetterService:
    def __init__(self, repository: StateRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
