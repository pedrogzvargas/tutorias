from shared.repositories import Repository
from tutorias_itsvc.common.models import Gender


class GenderRepository(Repository):
    def __init__(self, model=None):
        model = model or Gender
        super(GenderRepository, self).__init__(model)
