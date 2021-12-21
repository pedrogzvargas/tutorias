from tutorias_itsvc.students.repositories import MotivacionEstudioRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.services.student.exceptions import StudentNotExist
from tutorias_itsvc.students.services.motivacion_estudio.exceptions import MotivacionEstudioNotExist


class MotivacionEstudioDeleterService:
    def __init__(self,
                 motivacion_estudio_repository: MotivacionEstudioRepository,
                 student_repository: StudentRepository):
        self.__motivacion_estudio_repository = motivacion_estudio_repository
        self.__student_repository = student_repository

    def __call__(self, student_id):
        student = self.__student_repository.get(id=student_id)
        motivacion_estudio = self.__motivacion_estudio_repository.get(student_id=student_id)
        if not motivacion_estudio:
            raise MotivacionEstudioNotExist(f"No existe un registro de motivacion estudio "
                                            f"para el usuario con id {student_id}")
        if not student:
            raise StudentNotExist(f"No existe un estudiante con el id {student_id}")
        return self.__motivacion_estudio_repository.delete(id=motivacion_estudio.id)
