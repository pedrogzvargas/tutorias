from shared.repositories import Repository
from tutorias_itsvc.students.models import EstiloAprendizaje


class EstiloAprendizajeRepository(Repository):
    def __init__(self, model=None):
        model = model or EstiloAprendizaje
        super(EstiloAprendizajeRepository, self).__init__(model)
