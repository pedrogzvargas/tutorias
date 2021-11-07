from tutorias_itsvc.students.repositories import ParentRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.common.repositories import AcademicDegreeRepository
from tutorias_itsvc.students.services.parent.exceptions import ParentAlreadyExist
from tutorias_itsvc.common.services.academic_degree.exceptions import AcademicDegreeNotExist
from tutorias_itsvc.students.services.student.exceptions import StudentNotExist


class ParentCreatorService:
    def __init__(self,
                 parent_repository: ParentRepository,
                 student_repository: StudentRepository,
                 academic_degree_repository: AcademicDegreeRepository):
        self.__parent_repository = parent_repository
        self.__student_repository = student_repository
        self.__academic_degree_repository = academic_degree_repository

    def __call__(self,
                 student_id,
                 type,
                 first_name,
                 last_name,
                 birth_date,
                 academic_degree_id,
                 has_job,
                 profession_occupation,
                 is_alive,
                 second_name=None,
                 second_last_name=None,
                 workplace=None,
                 type_of_job=None,
                 address_id=None):

        if not self.__student_repository.get(id=student_id):
            raise StudentNotExist(f"No existe un estudiante con el id {student_id}")

        if not self.__academic_degree_repository.get(id=academic_degree_id):
            raise AcademicDegreeNotExist(f"No existe un nivel académico con el id {academic_degree_id}")

        if self.__parent_repository.get(student_id=student_id, type=type):
            raise ParentAlreadyExist(f"Ya existe un registro de {type} del estudiante con id {student_id}")

        return self.__parent_repository.create(student_id=student_id,
                                               type=type,
                                               first_name=first_name,
                                               second_name=second_name,
                                               last_name=last_name,
                                               second_last_name=second_last_name,
                                               birth_date=birth_date,
                                               academic_degree_id=academic_degree_id,
                                               has_job=has_job,
                                               workplace=workplace,
                                               type_of_job=type_of_job,
                                               profession_occupation=profession_occupation,
                                               is_alive=is_alive,
                                               address_id=address_id,
                                               )
