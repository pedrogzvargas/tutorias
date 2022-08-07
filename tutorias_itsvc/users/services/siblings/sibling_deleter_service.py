from tutorias_itsvc.users.repositories import SiblingRepository


class SiblingDeleterService:
    def __init__(self, repository: SiblingRepository):
        self.__repository = repository

    def __call__(self, id):
        return self.__repository.delete(id)
