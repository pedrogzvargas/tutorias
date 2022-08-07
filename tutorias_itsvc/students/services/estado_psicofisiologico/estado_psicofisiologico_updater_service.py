from tutorias_itsvc.students.repositories import EstadoPsicofisiologicoRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.services.student.exceptions import StudentNotExist
from tutorias_itsvc.students.services.estado_psicofisiologico.exceptions import EstadoPsicofisiologicoAlreadyExist


class EstadoPsicofisiologicoUpdaterService:
    def __init__(self,
                 estado_psicofisiologico_repository: EstadoPsicofisiologicoRepository,
                 student_repository: StudentRepository):
        self.__estado_psicofisiologico_repository = estado_psicofisiologico_repository
        self.__student_repository = student_repository

    def __call__(self, student_id, p1, p2, p3, p4, p5, p6, p7, p8, p9, p10, p11, p12, p8_1=None):
        student = self.__student_repository.get(id=student_id)
        estado_psicofisiologico = self.__estado_psicofisiologico_repository.get(student_id=student_id)
        if not estado_psicofisiologico:
            raise EstadoPsicofisiologicoAlreadyExist(f"No existe un registro de estado_psicofisiologico "
                                                     f"para el usuario con id {student_id}")
        if not student:
            raise StudentNotExist(f"No existe un estudiante con el id {student_id}")
        return self.__estado_psicofisiologico_repository.update(id=estado_psicofisiologico.id,
                                                                student_id=student_id,
                                                                p1=p1,
                                                                p2=p2,
                                                                p3=p3,
                                                                p4=p4,
                                                                p5=p5,
                                                                p6=p6,
                                                                p7=p7,
                                                                p8=p8,
                                                                p8_1=p8_1,
                                                                p9=p9,
                                                                p10=p10,
                                                                p11=p11,
                                                                p12=p12)
