from shared.repositories import Repository
from tutorias_itsvc.students.models import CaracteristicasPersonales


class CaracteristicasPersonalesRepository(Repository):
    def __init__(self, model=None):
        model = model or CaracteristicasPersonales
        super(CaracteristicasPersonalesRepository, self).__init__(model)
