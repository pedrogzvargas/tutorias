from tutorias_itsvc.users.services.group import GroupFilterService
from tutorias_itsvc.users.repositories import GroupRepository


class RoleGetterService:
    def __init__(self, user):
        self.__user = user

    def __call__(self):
        repository = GroupRepository()
        filter_service = GroupFilterService(repository)
        groups = filter_service()
        user_roles = list()
        for group in groups:
            role = getattr(self.__user, f"{group.name}", None)
            if role:
                user_roles.append(dict(name=group.name, id=role.id))
        return user_roles
