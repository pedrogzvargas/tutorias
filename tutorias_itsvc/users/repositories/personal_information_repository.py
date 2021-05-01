from tutorias_itsvc.users.models import PersonalInformation
from shared.repositories import Repository


class PersonalInformationRepository(Repository):

    def __init__(self, model=PersonalInformation):
        super(PersonalInformationRepository, self).__init__(model)
