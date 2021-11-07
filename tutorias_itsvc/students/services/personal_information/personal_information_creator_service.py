from tutorias_itsvc.students.services.student.exceptions import StudentNotExist
from tutorias_itsvc.common.services.gender.exceptions import GenderNotExist
from tutorias_itsvc.common.services.marital_status.exceptions import MaritalStatusNotExist


class PersonalInformationCreatorService:
    def __init__(self,
                 personal_information_repository=None,
                 student_repository=None,
                 gender_repository=None,
                 marital_status_repository=None):
        self.__personal_information_repository = personal_information_repository
        self.__student_repository = student_repository
        self.__gender_repository = gender_repository
        self.__marital_status_repository = marital_status_repository

    def __call__(self,
                 student_id,
                 place_birth,
                 birth_date,
                 has_children,
                 gender_id,
                 marital_status_id,
                 height,
                 weight,
                 number_of_children=None,
                 marital_status_description=None,
                 ):
        student = self.__student_repository.get(id=student_id)
        marital_status = self.__marital_status_repository.get(id=marital_status_id)
        gender = self.__gender_repository.get(id=gender_id)

        if not student:
            raise StudentNotExist(f"No se encontró el estudiante con el id {student_id}")

        if not marital_status:
            raise MaritalStatusNotExist(f"No se encontró el estado civil con el id {marital_status_id}")

        if not gender:
            raise GenderNotExist(f"No se encontró el genero con el id {gender_id}")

        return self.__personal_information_repository.create(
            user=student.user,
            place_birth=place_birth,
            birth_date=birth_date,
            has_children=has_children,
            gender_id=gender_id,
            marital_status_id=marital_status_id,
            height=height,
            weight=weight,
            number_of_children=number_of_children,
            marital_status_description=marital_status_description
        )
