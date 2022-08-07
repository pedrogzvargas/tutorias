class FullNameGetter:
    def __init__(self, user):
        self.__user = user

    def __call__(self):
        full_name = f"{self.__user.first_name or ''} {self.__user.second_name or ''} " \
                    f"{self.__user.last_name or ''} {self.__user.second_last_name or ''}"
        return full_name.strip()

