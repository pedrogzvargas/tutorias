from shared.repositories import Repository
from tutorias_itsvc.students.models import StudentAddress


class AddressRepository(Repository):
    def __init__(self, model=None):
        model = model or StudentAddress
        super(AddressRepository, self).__init__(model)
