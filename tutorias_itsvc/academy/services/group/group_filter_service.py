from tutorias_itsvc.academy.repositories import GroupRepository


class GroupFilterService:
    def __init__(self, repository: GroupRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.filter(**kwargs)
