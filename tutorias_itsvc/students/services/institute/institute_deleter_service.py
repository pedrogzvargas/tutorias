from tutorias_itsvc.students.repositories import StudentInstituteRepository
from tutorias_itsvc.students.services.institute.exceptions import InstituteNotExist


class InstituteDeleterService:
    def __init__(self,
                 student_institute_repository: StudentInstituteRepository):
        self.__student_institute_repository = student_institute_repository

    def __call__(self, institute_id, student_id):
        institute = self.__student_institute_repository.get(id=institute_id, student_id=student_id)
        if not institute:
            InstituteNotExist(f"No existe un instituto con el id {institute_id}")
        return self.__student_institute_repository.delete(id=institute_id)
