from tutorias_itsvc.users.models import Sibling
from shared.repositories import Repository


class SiblingRepository(Repository):

    def __init__(self, model=Sibling):
        super(SiblingRepository, self).__init__(model)
