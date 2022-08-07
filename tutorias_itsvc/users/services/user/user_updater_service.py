from tutorias_itsvc.users.repositories import UserRepository


class UserUpdaterService:
    def __init__(self, repository: UserRepository):
        self.__repository = repository

    def __call__(self, id, **kwargs):
        return self.__repository.update(id, **kwargs)
