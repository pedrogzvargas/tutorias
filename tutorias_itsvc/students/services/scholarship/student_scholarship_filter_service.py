from tutorias_itsvc.students.repositories import StudentScholarshipRepository


class StudentScholarshipFilterService:
    def __init__(self, repository: StudentScholarshipRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.filter(**kwargs)
