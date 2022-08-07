from tutorias_itsvc.users.repositories import UserRepository
from tutorias_itsvc.users.services.user.exceptions import UserNotExist


class UserProfileGetterService:
    def __init__(self, repository: UserRepository):
        self.__repository = repository

    def __call__(self, user_id):
        user = self.__repository.get(id=user_id)
        if not user:
            raise UserNotExist(f"No existe un usuario con el id {user_id}")
        return dict(
            id=user.id,
            first_name=user.first_name,
            last_name=user.last_name,
            second_name=user.second_name,
            second_last_name=user.second_last_name,
            email=user.email,
        )
