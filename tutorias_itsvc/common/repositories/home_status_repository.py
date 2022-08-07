from shared.repositories import Repository
from tutorias_itsvc.common.models import HomeStatus


class HomeStatusRepository(Repository):
    def __init__(self, model=None):
        model = model or HomeStatus
        super(HomeStatusRepository, self).__init__(model)
