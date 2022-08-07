from tutorias_itsvc.tutor.repositories import TutorRepository
from tutorias_itsvc.users.repositories import UserRepository


class TutorDeleterService:
    def __init__(self, tutor_repository: TutorRepository, user_repository: UserRepository):
        self.__tutor_repository = tutor_repository
        self.__user_repository = user_repository

    def __call__(self, tutor_id):
        tutor = self.__tutor_repository.get(id=tutor_id)
        if not tutor:
            raise Exception('No existe un tutor con este id')
        user = tutor.user
        self.__tutor_repository.delete(id=tutor_id)
        self.__user_repository.delete(id=user.id)
