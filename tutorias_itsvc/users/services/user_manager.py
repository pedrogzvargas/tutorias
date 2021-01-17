from django.contrib.auth import get_user_model
from tutorias_itsvc.utils import ModelPopulate

User = get_user_model()


class UserManager:
    def __init__(self, user: User):
        self.user = user

    def update(self, user_information: dict):
        print(user_information)
        self.user = ModelPopulate.populate(self.user, user_information)
        self.user.save()
        return self.user

    def delete(self):
        pass
