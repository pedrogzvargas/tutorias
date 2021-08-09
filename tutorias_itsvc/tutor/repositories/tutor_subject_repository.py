from tutorias_itsvc.tutor.models import TutorSubject
from shared.repositories import Repository


class TutorSubjectRepository(Repository):
    def __init__(self, model=None):
        model = model or TutorSubject
        super(TutorSubjectRepository, self).__init__(model)
