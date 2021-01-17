from django.contrib.auth.models import Group
from shared.repositories import Repository


class GroupRepository(Repository):

    def __init__(self, model=Group):
        super(GroupRepository, self).__init__(model)
