from django.contrib.auth.hashers import make_password
from django.db import transaction
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.users.repositories import UserRepository


class StudentUpdaterService:
    def __init__(self, student_repository: StudentRepository, user_repository: UserRepository):
        self.__student_repository = student_repository
        self.__user_repository = user_repository

    @transaction.atomic
    def __call__(self, student_id, **kwargs):
        username = kwargs.get('username')
        password = kwargs.get('password')
        student = self.__student_repository.get(id=student_id)
        if not student:
            raise Exception('No existe un usuario con este id')
        user_fields = dict(
            first_name=kwargs.get('first_name'),
            last_name=kwargs.get('last_name'),
            second_name=kwargs.get('second_name'),
            second_last_name=kwargs.get('second_last_name'),
            email=kwargs.get('email')
        )
        student_fields = dict()
        if password:
            user_fields.update(dict(password=make_password(password), ))

        if student.user.username != username:
            user_fields.update(dict(username=username))
            student_fields.update(dict(enrollment=username))

        self.__user_repository.update(id=student.user.id, **user_fields)
        return self.__student_repository.update(id=student.user.id, **student_fields)
