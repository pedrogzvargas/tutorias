from django.db import transaction
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.services.student.exceptions import StudentNotExist
from tutorias_itsvc.students.repositories import StudentPhoneRepository


class StudentPhonesCreatorOrUpdaterService:
    def __init__(self,
                 student_repository: StudentRepository,
                 student_phone_repository: StudentPhoneRepository):
        self.__student_repository = student_repository
        self.__student_phone_repository = student_phone_repository

    @transaction.atomic
    def __call__(self,
                 student_id,
                 home_phone=None,
                 mobile_phone=None):

        if not self.__student_repository.get(id=student_id):
            raise StudentNotExist(f"No existe un estudiante con el id {student_id}")

        phones = self.__student_phone_repository.filter(student_id=student_id)
        phones.delete()

        if home_phone:
            self.__student_phone_repository.create(student_id=student_id,
                                                   number=home_phone,
                                                   type="home_phone")

        if mobile_phone:
            self.__student_phone_repository.create(student_id=student_id,
                                                   number=mobile_phone,
                                                   type="mobile_phone")
