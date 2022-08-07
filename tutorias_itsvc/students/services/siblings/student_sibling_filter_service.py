from tutorias_itsvc.students.repositories import StudentSiblingRepository


class StudentSiblingFilterService:
    def __init__(self, repository: StudentSiblingRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.filter(**kwargs)
