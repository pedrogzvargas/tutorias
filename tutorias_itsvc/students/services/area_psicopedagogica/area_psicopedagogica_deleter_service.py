from tutorias_itsvc.students.repositories import AreaPsicopedagogicaRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.services.student.exceptions import StudentNotExist
from tutorias_itsvc.students.services.area_integracion.exceptions import AreaIntegracionNotExist


class AreaPsicopedagogicaDeleterService:
    def __init__(self,
                 area_psicopedagogica_repository: AreaPsicopedagogicaRepository,
                 student_repository: StudentRepository):
        self.__area_psicopedagogica_repository = area_psicopedagogica_repository
        self.__student_repository = student_repository

    def __call__(self, student_id):
        student = self.__student_repository.get(id=student_id)
        area_psicopedagogica = self.__area_psicopedagogica_repository.get(student_id=student_id)
        if not area_psicopedagogica:
            raise AreaIntegracionNotExist(f"No existe un registro de area psicopedagogica "
                                          f"para el usuario con id {student_id}")
        if not student:
            raise StudentNotExist(f"No existe un estudiante con el id {student_id}")
        return self.__area_psicopedagogica_repository.delete(id=area_psicopedagogica.id)
