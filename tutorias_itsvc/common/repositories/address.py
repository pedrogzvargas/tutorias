from shared.repositories import Repository
from tutorias_itsvc.common.models import Address


class AddressRepository(Repository):
    def __init__(self, model=None):
        model = model or Address
        super(AddressRepository, self).__init__(model)
