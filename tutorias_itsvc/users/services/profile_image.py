from tutorias_itsvc.users.models import ProfileImage as ProfileImageModel


class ProfileImage:
    def __init__(self, user):
        self.user = user

    def get(self):
        profile_image = ProfileImageModel.objects.filter(user=self.user).order_by('created_at').last()
        return profile_image
