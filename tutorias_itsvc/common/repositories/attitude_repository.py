from shared.repositories import Repository
from tutorias_itsvc.common.models import Attitude


class AttitudeRepository(Repository):
    def __init__(self, model=None):
        model = model or Attitude
        super(AttitudeRepository, self).__init__(model)
