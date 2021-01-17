from tutorias_itsvc.academy.models import PeriodNumber
from shared.repositories import Repository


class PeriodNumberRepository(Repository):
    def __init__(self, model=None):
        model = model or PeriodNumber
        super(PeriodNumberRepository, self).__init__(model)
