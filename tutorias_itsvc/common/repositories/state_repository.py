from shared.repositories import Repository
from tutorias_itsvc.common.models import State


class StateRepository(Repository):
    def __init__(self, model=None):
        model = model or State
        super(StateRepository, self).__init__(model)
