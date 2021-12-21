from tutorias_itsvc.students.repositories import AreaPsicopedagogicaRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.services.student.exceptions import StudentNotExist
from tutorias_itsvc.students.services.area_integracion.exceptions import AreaIntegracionAlreadyExist


class AreaPsicopedagogicaCreatorService:
    def __init__(self,
                 area_psicopedagogica_repository: AreaPsicopedagogicaRepository,
                 student_repository: StudentRepository):
        self.__area_psicopedagogica_repository = area_psicopedagogica_repository
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
                 p8_1,
                 p9,
                 p10,
                 p11,
                 p12,
                 p13,
                 p14,
                 p15,
                 p16):
        student = self.__student_repository.get(id=student_id)
        if self.__area_psicopedagogica_repository.get(student_id=student_id):
            raise AreaIntegracionAlreadyExist("Ya existe un registro")
        if not student:
            raise StudentNotExist(f"No existe un estudiante con el id {student_id}")
        return self.__area_psicopedagogica_repository.create(student_id=student_id,
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
                                                             p12=p12,
                                                             p13=p13,
                                                             p14=p14,
                                                             p15=p15,
                                                             p16=p16)
