from tutorias_itsvc.students.repositories import AddressRepository


class AddressUpdaterService:
    def __init__(self, repository: AddressRepository):
        self.__repository = repository

    def __call__(self, id, **kwargs):
        return self.__repository.update(id, **kwargs)
