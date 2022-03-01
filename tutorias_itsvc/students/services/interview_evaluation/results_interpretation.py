class ResultInterpretation:
    def __init__(self, value):
        self.__value = value

    def __call__(self):
        if 0 <= self.__value <= 33:
            result = "Muy bajo"
        elif 34 <= self.__value <= 36:
            result = "Bajo"
        elif 37 <= self.__value <= 38:
            result = "Por debajo del promedio"
        elif 39 <= self.__value <= 42:
            result = "Promedio bajo"
        elif 43 <= self.__value <= 47:
            result = "Promedio"
        elif 48 <= self.__value <= 49:
            result = "Promedio alto"
        elif 50 <= self.__value <= 51:
            result = "Por encima del promedio"
        elif 52 <= self.__value <= 56:
            result = "Por encima del promedio"
        elif 57 <= self.__value <= 60:
            result = "Por encima del promedio"
        else:
            result = "Evaluación invalida"

        return result
