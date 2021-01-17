from tutorias_itsvc.users.repositories import UserRepository


class UserCreatorService:
    def __init__(self, repository: UserRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.create(**kwargs)
