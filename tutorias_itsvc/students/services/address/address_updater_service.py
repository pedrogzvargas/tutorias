from tutorias_itsvc.students.repositories import AddressRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.services.student.exceptions import StudentNotExist
from tutorias_itsvc.students.services.address.exceptions import AddressNotExist


class AddressUpdaterService:
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
        address = self.__address_repository.get(student_id=student_id)
        if not address:
            raise AddressNotExist(f"No existe una dirección registrada con el id de estudiante {student_id}")

        student = self.__student_repository.get(id=student_id)
        if not student:
            raise StudentNotExist(f"No existe un estudiante con el id {student_id}")

        return self.__address_repository.update(
            id=address.id,
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
