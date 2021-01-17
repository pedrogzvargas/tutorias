from tutorias_itsvc.academy.models import Group
from shared.repositories import Repository


class GroupRepository(Repository):
    def __init__(self, model=None):
        model = model or Group
        super(GroupRepository, self).__init__(model)
