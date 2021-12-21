from tutorias_itsvc.students.repositories import OrganizacionEstudioRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.services.student.exceptions import StudentNotExist
from tutorias_itsvc.students.services.organizacion_estudio.exceptions import OrganizacionEstudioNotExist


class OrganizacionEstudioDeleterService:
    def __init__(self,
                 organizacion_estudio_repository: OrganizacionEstudioRepository,
                 student_repository: StudentRepository):
        self.__organizacion_estudio_repository = organizacion_estudio_repository
        self.__student_repository = student_repository

    def __call__(self, student_id):
        student = self.__student_repository.get(id=student_id)
        organizacion_estudio = self.__organizacion_estudio_repository.get(student_id=student_id)
        if not organizacion_estudio:
            raise OrganizacionEstudioNotExist(f"No existe un registro de motivacion estudio "
                                              f"para el usuario con id {student_id}")
        if not student:
            raise StudentNotExist(f"No existe un estudiante con el id {student_id}")
        return self.__organizacion_estudio_repository.delete(id=organizacion_estudio.id)
