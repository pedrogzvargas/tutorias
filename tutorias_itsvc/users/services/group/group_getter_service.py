from tutorias_itsvc.users.repositories import GroupRepository


class GroupGetterService:
    def __init__(self, repository: GroupRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
