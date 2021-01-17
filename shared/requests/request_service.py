from shared.exceptions import SerializerApiException


class RequestService:
    def __init__(self, payload, serializer_class):
        self.__serializer = serializer_class(data=payload)

    def get_data(self):
        if not self.__serializer.is_valid():
            raise SerializerApiException("Invalid Data", 400, self.__serializer.errors)

        return self.__serializer.data
