from tutorias_itsvc.common.repositories import AddressRepository


class AddressGetterService:
    def __init__(self, repository: AddressRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
