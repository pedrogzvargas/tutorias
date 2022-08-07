from tutorias_itsvc.tutor.models import Tutor
from shared.repositories import Repository


class TutorRepository(Repository):
    def __init__(self, model=None):
        model = model or Tutor
        super(TutorRepository, self).__init__(model)
