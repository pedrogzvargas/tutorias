class GetterSerializerService:
    def __init__(self, serializer_class=None, many=False, context={}):
        self.__context = context
        self.__serializer_class = serializer_class
        self.__many = many

    def __call__(self, model_instance):
        if model_instance is None:
            return None
        serializer = self.__serializer_class(model_instance, many=self.__many, context=self.__context)

        return serializer.data
