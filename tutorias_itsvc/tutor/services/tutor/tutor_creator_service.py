from django.contrib.auth.hashers import make_password
from django.db import transaction
from tutorias_itsvc.tutor.repositories import TutorRepository
from tutorias_itsvc.users.repositories import UserRepository
from tutorias_itsvc.users.repositories import GroupRepository


class TutorCreatorService:
    def __init__(self,
                 tutor_repository: TutorRepository,
                 user_repository: UserRepository,
                 group_repository: GroupRepository):
        self.__tutor_repository = tutor_repository
        self.__user_repository = user_repository
        self.__group_repository = group_repository

    @transaction.atomic
    def __call__(self, **kwargs):
        username = kwargs.get('username')
        user = self.__user_repository.get(username=username)
        if user:
            raise Exception('Ya existe un usuario con este nombre de usuario')
        user = self.__user_repository.create(
            username=username,
            password=make_password(kwargs.get('password')),
            first_name=kwargs.get('first_name'),
            last_name=kwargs.get('last_name'),
            second_name=kwargs.get('second_name'),
            second_last_name=kwargs.get('second_last_name'),
            email=kwargs.get('email', '')
        )
        tutors_group = self.__group_repository.get(name="tutor")
        if not tutors_group:
            raise Exception("No existe el grupo para tutores")
        user.groups.add(tutors_group)
        return self.__tutor_repository.create(user=user,
                                              enrollment=username,
                                              academic_id=kwargs.get("academic_id"),
                                              is_active=kwargs.get('is_active'))
