from shared.repositories import Repository
from tutorias_itsvc.common.models import SchoolCycle


class SchoolCycleRepository(Repository):
    def __init__(self, model=None):
        model = model or SchoolCycle
        super(SchoolCycleRepository, self).__init__(model)
