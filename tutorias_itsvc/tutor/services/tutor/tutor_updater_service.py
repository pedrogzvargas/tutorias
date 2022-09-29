from django.contrib.auth.hashers import make_password
from django.db import transaction
from tutorias_itsvc.tutor.repositories import TutorRepository
from tutorias_itsvc.users.repositories import UserRepository


class TutorUpdaterService:
    def __init__(self, tutor_repository: TutorRepository, user_repository: UserRepository):
        self.__tutor_repository = tutor_repository
        self.__user_repository = user_repository

    @transaction.atomic
    def __call__(self, tutor_id,  **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')
        tutor = self.__tutor_repository.get(id=tutor_id)
        if not tutor:
            raise Exception('No existe un tutor con este id')

        user_fields = dict(
            first_name=kwargs.get('first_name'),
            last_name=kwargs.get('last_name'),
            second_name=kwargs.get('second_name'),
            second_last_name=kwargs.get('second_last_name'),
            email=kwargs.get('email', '')
        )

        tutor_fields = dict(
            academic_id=kwargs.get("academic_id"),
            is_active=kwargs.get('is_active')
        )
        if password:
            user_fields.update(dict(password=make_password(password), ))

        if tutor.user.username != username:
            user_fields.update(dict(username=username))
            tutor_fields.update(dict(enrollment=username))

        print(tutor_fields)
        self.__user_repository.update(id=tutor.user.id, **user_fields)
        return self.__tutor_repository.update(id=tutor.id, **tutor_fields)
