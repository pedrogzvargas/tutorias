from tutorias_itsvc.students.repositories import TecnicaEstudioRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.services.student.exceptions import StudentNotExist
from tutorias_itsvc.students.services.tecnica_estudio.exceptions import TecnicaEstudioNotExist


class TecnicaEstudioDeleterService:
    def __init__(self,
                 tecnica_estudio_repository: TecnicaEstudioRepository,
                 student_repository: StudentRepository):
        self.__tecnica_estudio_repository = tecnica_estudio_repository
        self.__student_repository = student_repository

    def __call__(self, student_id):
        student = self.__student_repository.get(id=student_id)
        tecnica_estudio = self.__tecnica_estudio_repository.get(student_id=student_id)
        if not tecnica_estudio:
            raise TecnicaEstudioNotExist(f"No existe un registro de tecnica estudio "
                                         f"para el usuario con id {student_id}")
        if not student:
            raise StudentNotExist(f"No existe un estudiante con el id {student_id}")
        return self.__tecnica_estudio_repository.delete(id=tecnica_estudio.id)
