from tutorias_itsvc.students.repositories import ParentRepository
from tutorias_itsvc.students.services.parent.exceptions import ParentNotExist


class ParentDeleterService:
    def __init__(self, parent_repository: ParentRepository):
        self.__parent_repository = parent_repository

    def __call__(self, student_id, type):
        parent = self.__parent_repository.get(student_id=student_id, type=type)
        if not parent:
            raise ParentNotExist(f"No existe un registro de {type} del estudiante con id {student_id}")
        return self.__parent_repository.delete(id=parent.id)
