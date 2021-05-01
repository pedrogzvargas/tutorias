from tutorias_itsvc.students.repositories import AddressRepository


class AddressCreatorService:
    def __init__(self, repository: AddressRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.create(**kwargs)
