from shared.repositories import Repository
from tutorias_itsvc.common.models import HousingType


class HousingTypeRepository(Repository):
    def __init__(self, model=None):
        model = model or HousingType
        super(HousingTypeRepository, self).__init__(model)
