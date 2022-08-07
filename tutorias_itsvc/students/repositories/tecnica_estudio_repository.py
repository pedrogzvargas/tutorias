from shared.repositories import Repository
from tutorias_itsvc.students.models import TecnicaEstudio


class TecnicaEstudioRepository(Repository):
    def __init__(self, model=None):
        model = model or TecnicaEstudio
        super(TecnicaEstudioRepository, self).__init__(model)
