from tutorias_itsvc.students.repositories import CaracteristicasPersonalesRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.services.student.exceptions import StudentNotExist
from tutorias_itsvc.students.services.caracteristicas_personales.exceptions import CaracteristicasPersonalesNotExist


class CaracteristicasPersonalesDeleterService:
    def __init__(self,
                 caracteristicas_personales_repository: CaracteristicasPersonalesRepository,
                 student_repository: StudentRepository):
        self.__caracteristicas_personales_repository = caracteristicas_personales_repository
        self.__student_repository = student_repository

    def __call__(self, student_id):
        student = self.__student_repository.get(id=student_id)
        caracteristicas_personales = self.__caracteristicas_personales_repository.get(student_id=student_id)
        if not caracteristicas_personales:
            raise CaracteristicasPersonalesNotExist(f"No existe un registro de caracteristicas_personales "
                                                    f"para el usuario con id {student_id}")
        if not student:
            raise StudentNotExist(f"No existe un estudiante con el id {student_id}")
        return self.__caracteristicas_personales_repository.delete(id=caracteristicas_personales.id)
