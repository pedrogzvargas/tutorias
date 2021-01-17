class AllSerializerService:
    def __init__(self, serializer_class=None):
        self.__serializer_class = serializer_class

    def __call__(self, data):
        if data is None:
            return None
        serializer = self.__serializer_class(data, many=True)

        return serializer.data
