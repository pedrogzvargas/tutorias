import pandas as pd
from io import BytesIO
import base64
from django.contrib.auth.hashers import make_password
from django.db import transaction
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.repositories import AcademicInformationRepository
from tutorias_itsvc.users.repositories import UserRepository
from tutorias_itsvc.users.repositories import GroupRepository
from tutorias_itsvc.academy.repositories import AcademicGroupRepository


class StudentsLoaderService:
    def __init__(
        self,
        student_repository: StudentRepository,
        user_repository: UserRepository,
        group_repository: GroupRepository,
        academic_group_repository: AcademicGroupRepository,
        academic_information_repository: AcademicInformationRepository,
    ):
        self.__student_repository = student_repository
        self.__user_repository = user_repository
        self.__group_repository = group_repository
        self.__academic_group_repository = academic_group_repository
        self.__academic_information_repository = academic_information_repository

    @transaction.atomic
    def __call__(self, **kwargs):
        base64_as_string = kwargs.get('file')
        file_as_bytes = base64.b64decode(base64_as_string)
        data_frame = pd.read_csv(BytesIO(file_as_bytes), keep_default_na=False)
        dataframe_as_dict = data_frame.to_dict(orient='records')
        for student in dataframe_as_dict:
            username = student.get('enrollment')
            user = self.__user_repository.get(username=username)
            if user:
                raise Exception(f'Ya existe un usuario con este nombre de usuario {username}')
            user = self.__user_repository.create(
                username=username,
                password=make_password(student.get('enrollment')),
                first_name=student.get('first_name'),
                last_name=student.get('last_name'),
                second_name=student.get('second_name'),
                second_last_name=student.get('second_last_name'),
                email=student.get('email')
            )
            students_group = self.__group_repository.get(name="student")
            if not students_group:
                raise Exception("No existe el grupo para estudiantes")
            user.groups.add(students_group)
            academic_information = self.__academic_group_repository.get(
                academic_period_number__academic_period__academic_major__university__acronym=student.get('university'),
                academic_period_number__academic_period__academic_major__major__name=student.get('major'),
                academic_period_number__academic_period__period__name=student.get('period'),
                academic_period_number__period_number__name=student.get('period_number'),
                group__name=student.get('group')
            )
            if not academic_information:
                raise Exception(f"No existe la información academica del usuario {username}")
            student = self.__student_repository.create(user_id=user.id, enrollment=username)
            self.__academic_information_repository.create(student_id=student.id, academic_information_id=academic_information.id)
