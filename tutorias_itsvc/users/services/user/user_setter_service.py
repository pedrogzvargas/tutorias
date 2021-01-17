from tutorias_itsvc.users.repositories import UserRepository


class UserSetterService:
    def __init__(self, repository: UserRepository):
        self.__repository = repository

    def __call__(self, user_id, **kwargs):
        return self.__repository.update(user_id, **kwargs)
