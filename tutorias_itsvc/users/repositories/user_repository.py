from shared.repositories import Repository
from tutorias_itsvc.users.models import User


class UserRepository(Repository):
    def __init__(self, model=None):
        model = model or User
        super(UserRepository, self).__init__(model)
