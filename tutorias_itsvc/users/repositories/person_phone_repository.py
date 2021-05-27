from tutorias_itsvc.users.models import PersonPhone
from shared.repositories import Repository


class PersonPhoneRepository(Repository):

    def __init__(self, model=PersonPhone):
        super(PersonPhoneRepository, self).__init__(model)
