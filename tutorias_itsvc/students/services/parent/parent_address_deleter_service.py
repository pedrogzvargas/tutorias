from tutorias_itsvc.students.repositories import ParentRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.common.repositories import AddressRepository
from tutorias_itsvc.students.services.parent.exceptions import ParentNotExist
from tutorias_itsvc.students.services.student.exceptions import StudentNotExist
from tutorias_itsvc.common.services.address.exceptions import AddressNotExist


class ParentAddressDeleterService:
    def __init__(self,
                 parent_repository: ParentRepository,
                 student_repository: StudentRepository,
                 address_repository: AddressRepository):
        self.__parent_repository = parent_repository
        self.__student_repository = student_repository
        self.__address_repository = address_repository

    def __call__(self, student_id, type):
        if not self.__student_repository.get(id=student_id):
            raise StudentNotExist(f"No existe un estudiante con el id {student_id}")

        parent = self.__parent_repository.get(student_id=student_id, type=type)
        if not parent:
            raise ParentNotExist(f"No existe un registro de {type} del estudiante con id {student_id}")

        if not parent.address_id:
            raise AddressNotExist(f"No existe una dirección para el {type} de estudiante con id {student_id}")

        return self.__address_repository.delete(id=parent.address_id)
