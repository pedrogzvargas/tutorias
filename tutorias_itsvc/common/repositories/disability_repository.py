from shared.repositories import Repository
from tutorias_itsvc.common.models import Disability


class DisabilityRepository(Repository):
    def __init__(self, model=None):
        model = model or Disability
        super(DisabilityRepository, self).__init__(model)
