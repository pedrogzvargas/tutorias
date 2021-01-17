from tutorias_itsvc.academy.models import Period
from shared.repositories import Repository


class PeriodRepository(Repository):
    def __init__(self, model=None):
        model = model or Period
        super(PeriodRepository, self).__init__(model)
