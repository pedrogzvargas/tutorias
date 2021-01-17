from tutorias_itsvc.users.models import User as UserModel


class User:
    @staticmethod
    def get_all():
        users = UserModel.objects.all().order_by('pk')
        return users

    @staticmethod
    def get_by_id(user_id: int):
        user = UserModel.objects.get(pk=user_id)
        return user
