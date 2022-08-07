from django.db import transaction
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.users.repositories import UserRepository


class StudentDeleterService:
    def __init__(self, student_repository: StudentRepository, user_repository: UserRepository):
        self.__student_repository = student_repository
        self.__user_repository = user_repository

    @transaction.atomic
    def __call__(self, student_id):
        student = self.__student_repository.get(id=student_id)
        if not student:
            raise Exception('No existe un usuario con este id')
        user = student.user
        self.__student_repository.delete(id=student_id)
        self.__user_repository.delete(id=user.id)
