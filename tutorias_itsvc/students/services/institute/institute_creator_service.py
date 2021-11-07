from tutorias_itsvc.students.repositories import StudentInstituteRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.services.student.exceptions import StudentNotExist
from tutorias_itsvc.common.repositories import AcademicDegreeRepository
from tutorias_itsvc.common.services.academic_degree.exceptions import AcademicDegreeNotExist


class InstituteCreatorService:
    def __init__(self,
                 student_institute_repository: StudentInstituteRepository,
                 student_repository: StudentRepository,
                 academic_degree_repository: AcademicDegreeRepository):
        self.__student_institute_repository = student_institute_repository
        self.__student_repository = student_repository
        self.__academic_degree_repository = academic_degree_repository

    def __call__(self, student_id, institute_name, academic_degree_id, start_date, end_date):
        student = self.__student_repository.get(id=student_id)
        if not student:
            raise StudentNotExist(f"No existe estudiante con id {student_id}")
        academic_degree = self.__academic_degree_repository.get(id=academic_degree_id)
        if not academic_degree:
            raise AcademicDegreeNotExist(f"No existe un nivel académico con id {academic_degree_id}")
        return self.__student_institute_repository.create(
            student_id=student_id,
            institute_name=institute_name,
            academic_degree_id=academic_degree_id,
            start_date=start_date,
            end_date=end_date,
        )
