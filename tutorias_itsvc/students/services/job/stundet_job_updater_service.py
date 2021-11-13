from tutorias_itsvc.students.repositories import StudentJobRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.services.student.exceptions import StudentNotExist
from tutorias_itsvc.students.services.job.exceptions import JobNotExist


class StudentJobUpdaterService:
    def __init__(self, student_job_repository: StudentJobRepository, student_repository: StudentRepository):
        self.__student_job_repository = student_job_repository
        self.__student_repository = student_repository

    def __call__(self, student_id, has_job, company_name, schedule):
        student_job = self.__student_job_repository.get(student_id=student_id)
        if not student_job:
            raise JobNotExist(f"No existe un registro de trabajo para el usuario con id {student_id}")
        student = self.__student_repository.get(id=student_id)
        if not student:
            raise StudentNotExist(f"No existe estudiante con id {student_id}")
        return self.__student_job_repository.update(
            id=student_job.id,
            student_id=student_id,
            has_job=has_job,
            company_name=company_name,
            schedule=schedule
        )
