from django.db import transaction
from tutorias_itsvc.students.repositories import ParentRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.services.parent.exceptions import ParentNotExist
from tutorias_itsvc.students.services.student.exceptions import StudentNotExist
from tutorias_itsvc.users.repositories import PersonPhoneRepository


class ParentPhonesCreatorOrUpdaterService:
    def __init__(self,
                 parent_repository: ParentRepository,
                 student_repository: StudentRepository,
                 person_phone_repository: PersonPhoneRepository):
        self.__parent_repository = parent_repository
        self.__student_repository = student_repository
        self.__person_phone_repository = person_phone_repository

    @transaction.atomic
    def __call__(self,
                 student_id,
                 type,
                 home_phone=None,
                 mobile_phone=None):

        if not self.__student_repository.get(id=student_id):
            raise StudentNotExist(f"No existe un estudiante con el id {student_id}")

        parent = self.__parent_repository.get(student_id=student_id, type=type)
        if not parent:
            raise ParentNotExist(f"No existe un registro de {type} del estudiante con id {student_id}")

        phones = self.__person_phone_repository.filter(person_id=parent.id)
        phones.delete()

        if home_phone:
            self.__person_phone_repository.create(person_id=parent.id,
                                                  number=home_phone,
                                                  type="home_phone")

        if mobile_phone:
            self.__person_phone_repository.create(person_id=parent.id,
                                                  number=mobile_phone,
                                                  type="mobile_phone")
