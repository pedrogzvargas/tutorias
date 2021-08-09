from shared.repositories import Repository
from tutorias_itsvc.common.models import Income


class IncomeRepository(Repository):
    def __init__(self, model=None):
        model = model or Income
        super(IncomeRepository, self).__init__(model)
