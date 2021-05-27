from tutorias_itsvc.users.repositories import SiblingRepository


class SiblingGetterService:
    def __init__(self, repository: SiblingRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
