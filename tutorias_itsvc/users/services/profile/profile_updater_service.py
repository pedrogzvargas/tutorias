from tutorias_itsvc.users.repositories import UserRepository
from tutorias_itsvc.users.services.user.exceptions import UserNotExist


class UserProfileUpdaterService:
    def __init__(self, user_repository: UserRepository):
        self.__user_repository = user_repository

    def __call__(self, user_id, first_name, last_name, second_name=None, second_last_name=None, email=None):
        user = self.__user_repository.get(id=user_id)
        if not user:
            raise UserNotExist(f"No existe un usuario con el id {user_id}")
        return self.__user_repository.update(id=user.id,
                                             first_name=first_name,
                                             last_name=last_name,
                                             second_name=second_name,
                                             second_last_name=second_last_name,
                                             email=email)
