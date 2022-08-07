from tutorias_itsvc.students.repositories import StudentPhoneRepository


class PhoneUpdaterService:
    def __init__(self, repository: StudentPhoneRepository):
        self.__repository = repository

    def __call__(self, id, **kwargs):
        return self.__repository.update(id, **kwargs)
