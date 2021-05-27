from tutorias_itsvc.students.repositories import StudentSiblingRepository


class StudentSiblingCreatorService:
    def __init__(self, repository: StudentSiblingRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.create(**kwargs)
