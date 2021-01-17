from shared.repositories import Repository
from tutorias_itsvc.users.models import ProfileImage


class ProfileImageRepository(Repository):

    def __init__(self, model=ProfileImage):
        super(ProfileImageRepository, self).__init__(model)
