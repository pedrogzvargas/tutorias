from tutorias_itsvc.students.repositories import StudentPhoneRepository


class PhoneGetterService:
    def __init__(self, repository: StudentPhoneRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
