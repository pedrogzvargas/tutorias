from tutorias_itsvc.common.repositories import AddressRepository


class AddressDeleterService:
    def __init__(self, repository: AddressRepository):
        self.__repository = repository

    def __call__(self, id):
        return self.__repository.delete(id)
