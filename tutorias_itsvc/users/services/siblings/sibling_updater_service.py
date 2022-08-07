from tutorias_itsvc.users.repositories import SiblingRepository


class SiblingUpdaterService:
    def __init__(self, repository: SiblingRepository):
        self.__repository = repository

    def __call__(self, id, **kwargs):
        return self.__repository.update(id, **kwargs)
