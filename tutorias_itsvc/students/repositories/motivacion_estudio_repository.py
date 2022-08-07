from shared.repositories import Repository
from tutorias_itsvc.students.models import MotivacionEstudio


class MotivacionEstudioRepository(Repository):
    def __init__(self, model=None):
        model = model or MotivacionEstudio
        super(MotivacionEstudioRepository, self).__init__(model)
