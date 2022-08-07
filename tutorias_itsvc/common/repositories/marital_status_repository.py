from shared.repositories import Repository
from tutorias_itsvc.common.models import MaritalStatus


class MaritalStatusRepository(Repository):
    def __init__(self, model=None):
        model = model or MaritalStatus
        super(MaritalStatusRepository, self).__init__(model)
