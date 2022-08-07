from tutorias_itsvc.students.repositories import EstiloAprendizajeRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.services.student.exceptions import StudentNotExist
from tutorias_itsvc.students.services.estilo_aprendizaje.exceptions import EstiloAprendizajeNotExist


class EstiloAprendizajeDeleterService:
    def __init__(self,
                 estilo_aprendizaje_repository: EstiloAprendizajeRepository,
                 student_repository: StudentRepository):
        self.__estilo_aprendizaje_repository = estilo_aprendizaje_repository
        self.__student_repository = student_repository

    def __call__(self, student_id):
        student = self.__student_repository.get(id=student_id)
        estilo_aprendizaje = self.__estilo_aprendizaje_repository.get(student_id=student_id)
        if not estilo_aprendizaje:
            raise EstiloAprendizajeNotExist(f"No existe un registro de estilo aprendizaje "
                                            f"para el usuario con id {student_id}")
        if not student:
            raise StudentNotExist(f"No existe un estudiante con el id {student_id}")
        return self.__estilo_aprendizaje_repository.delete(id=estilo_aprendizaje.id)
