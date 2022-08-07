from tutorias_itsvc.students.repositories import TecnicaEstudioRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.services.student.exceptions import StudentNotExist
from tutorias_itsvc.students.services.tecnica_estudio.exceptions import TecnicaEstudioNotExist


class TecnicaEstudioUpdaterService:
    def __init__(self,
                 tecnica_estudio_repository: TecnicaEstudioRepository,
                 student_repository: StudentRepository):
        self.__tecnica_estudio_repository = tecnica_estudio_repository
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
                 p20):
        student = self.__student_repository.get(id=student_id)
        tecnica_estudio = self.__tecnica_estudio_repository.get(student_id=student_id)
        if not tecnica_estudio:
            raise TecnicaEstudioNotExist(f"No existe un registro de tecnica estudio "
                                         f"para el usuario con id {student_id}")
        if not student:
            raise StudentNotExist(f"No existe un estudiante con el id {student_id}")
        return self.__tecnica_estudio_repository.update(id=tecnica_estudio.id,
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
                                                        p20=p20)
