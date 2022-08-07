from tutorias_itsvc.students.repositories import ParentRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.common.repositories import StateRepository
from tutorias_itsvc.common.repositories import AddressRepository
from tutorias_itsvc.students.services.parent.exceptions import ParentNotExist
from tutorias_itsvc.students.services.student.exceptions import StudentNotExist
from tutorias_itsvc.common.services.state.exceptions import StateNotExist
from tutorias_itsvc.common.services.address.exceptions import AddressNotExist


class ParentAddressUpdaterService:
    def __init__(self,
                 parent_repository: ParentRepository,
                 student_repository: StudentRepository,
                 address_repository: AddressRepository,
                 state_repository: StateRepository):
        self.__parent_repository = parent_repository
        self.__student_repository = student_repository
        self.__address_repository = address_repository
        self.__state_repository = state_repository

    def __call__(self,
                 student_id,
                 type,
                 street,
                 outdoor_number,
                 colony,
                 locality,
                 state_id,
                 zip_code,
                 indoor_number=None):

        if not self.__student_repository.get(id=student_id):
            raise StudentNotExist(f"No existe un estudiante con el id {student_id}")

        parent = self.__parent_repository.get(student_id=student_id, type=type)
        if not parent:
            raise ParentNotExist(f"No existe un registro de {type} del estudiante con id {student_id}")

        if not parent.address_id:
            raise AddressNotExist(f"No existe una dirección para el {type} de estudiante con id {student_id}")

        if not self.__state_repository.get(id=state_id):
            raise StateNotExist(f"No existe un estado con el id {state_id}")

        return self.__address_repository.update(
            id=parent.address_id,
            street=street,
            outdoor_number=outdoor_number,
            indoor_number=indoor_number,
            colony=colony,
            locality=locality,
            state_id=state_id,
            zip_code=zip_code
        )
