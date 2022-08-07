from tutorias_itsvc.students.repositories import EstiloAprendizajeRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.services.student.exceptions import StudentNotExist
from tutorias_itsvc.students.services.estilo_aprendizaje.exceptions import EstiloAprendizajeNotExist


class EstiloAprendizajeUpdaterService:
    def __init__(self,
                 estilo_aprendizaje_repository: EstiloAprendizajeRepository,
                 student_repository: StudentRepository):
        self.__estilo_aprendizaje_repository = estilo_aprendizaje_repository
        self.__student_repository = student_repository

    def __call__(self,
                 student_id,
                 p1,
                 p2,
                 p3,
                 p4,
                 p5,
                 p6,
                 p7,
                 p8,
                 p9,
                 p10,
                 p11,
                 p12,
                 p13,
                 p14,
                 p15,
                 p16,
                 p17,
                 p18,
                 p19,
                 p20,
                 p21,
                 p22,
                 p23,
                 p24,
                 ):
        student = self.__student_repository.get(id=student_id)
        estilo_aprendizaje = self.__estilo_aprendizaje_repository.get(student_id=student_id)
        if not estilo_aprendizaje:
            raise EstiloAprendizajeNotExist(f"No existe un registro de estilo_aprendizaje "
                                            f"para el usuario con id {student_id}")
        if not student:
            raise StudentNotExist(f"No existe un estudiante con el id {student_id}")
        return self.__estilo_aprendizaje_repository.update(id=estilo_aprendizaje.id,
                                                           p1=p1,
                                                           p2=p2,
                                                           p3=p3,
                                                           p4=p4,
                                                           p5=p5,
                                                           p6=p6,
                                                           p7=p7,
                                                           p8=p8,
                                                           p9=p9,
                                                           p10=p10,
                                                           p11=p11,
                                                           p12=p12,
                                                           p13=p13,
                                                           p14=p14,
                                                           p15=p15,
                                                           p16=p16,
                                                           p17=p17,
                                                           p18=p18,
                                                           p19=p19,
                                                           p20=p20,
                                                           p21=p21,
                                                           p22=p22,
                                                           p23=p23,
                                                           p24=p24)
