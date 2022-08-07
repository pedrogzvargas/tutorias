from tutorias_itsvc.students.repositories import AddressRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.services.student.exceptions import StudentNotExist
from tutorias_itsvc.students.services.address.exceptions import AddressAlreadyExist


class AddressCreatorService:
    def __init__(self, address_repository: AddressRepository, student_repository: StudentRepository):
        self.__address_repository = address_repository
        self.__student_repository = student_repository

    def __call__(self,
                 student_id,
                 street,
                 outdoor_number,
                 indoor_number,
                 colony,
                 locality,
                 state_id,
                 zip_code,
                 housing_type_id,
                 home_status_id,
                 family_relationship,
                 members,
                 home_status_description=None
                 ):
        student = self.__student_repository.get(id=student_id)
        if self.__address_repository.get(student_id=student_id):
            raise AddressAlreadyExist("Ya existe una dirección registrada")
        if not student:
            raise StudentNotExist(f"No existe un usuario con el id {student_id}")
        return self.__address_repository.create(
            student_id=student_id,
            street=street,
            outdoor_number=outdoor_number,
            indoor_number=indoor_number,
            colony=colony,
            locality=locality,
            state_id=state_id,
            zip_code=zip_code,
            housing_type_id=housing_type_id,
            home_status_id=home_status_id,
            family_relationship=family_relationship,
            members=members,
            home_status_description=home_status_description
        )
