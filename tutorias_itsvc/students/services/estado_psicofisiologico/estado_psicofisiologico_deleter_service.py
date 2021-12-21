from tutorias_itsvc.students.repositories import EstadoPsicofisiologicoRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.services.student.exceptions import StudentNotExist
from tutorias_itsvc.students.services.estado_psicofisiologico.exceptions import EstadoPsicofisiologicoAlreadyExist


class EstadoPsicofisiologicoDeleterService:
    def __init__(self,
                 estado_psicofisiologico_repository: EstadoPsicofisiologicoRepository,
                 student_repository: StudentRepository):
        self.__estado_psicofisiologico_repository = estado_psicofisiologico_repository
        self.__student_repository = student_repository

    def __call__(self, student_id):
        student = self.__student_repository.get(id=student_id)
        estado_psicofisiologico = self.__estado_psicofisiologico_repository.get(student_id=student_id)
        if not estado_psicofisiologico:
            raise EstadoPsicofisiologicoAlreadyExist(f"No existe un registro de estado_psicofisiologico "
                                                     f"para el usuario con id {student_id}")
        if not student:
            raise StudentNotExist(f"No existe un estudiante con el id {student_id}")
        return self.__estado_psicofisiologico_repository.delete(id=estado_psicofisiologico.id)
