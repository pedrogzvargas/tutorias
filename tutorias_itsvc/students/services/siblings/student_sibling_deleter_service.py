from tutorias_itsvc.students.repositories import StudentSiblingRepository
from tutorias_itsvc.users.repositories import SiblingRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.services.student.exceptions import StudentNotExist
from tutorias_itsvc.students.services.siblings.exceptions import SiblingNotExist


class StudentSiblingDeleterService:
    def __init__(self,
                 sibling_repository: SiblingRepository,
                 student_repository: StudentRepository,
                 student_sibling_repository: StudentSiblingRepository):
        self.__sibling_repository = sibling_repository
        self.__student_repository = student_repository
        self.__student_sibling_repository = student_sibling_repository

    def __call__(self, student_id, sibling_id):

        if not self.__student_sibling_repository.get(student_id=student_id, sibling_id=sibling_id):
            raise SiblingNotExist(f"No existe un usuario de hermano con id {sibling_id}")

        if not self.__student_repository.get(id=student_id):
            raise StudentNotExist(f"No existe un estudiante con el id {student_id}")

        return self.__sibling_repository.delete(id=sibling_id)
