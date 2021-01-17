from tutorias_itsvc.users.models import ProfileImage
from tutorias_itsvc.utils import ModelPopulate


class ProfileImageManager:
    def __init__(self, user):
        self.user = user

    def create(self, profile_image_info):
        profile_image = ProfileImage()
        profile_image.user = self.user
        profile_image = ModelPopulate.populate(profile_image, profile_image_info)
        profile_image.save()
        return profile_image
