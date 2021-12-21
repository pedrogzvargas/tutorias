from tutorias_itsvc.courses.repositories import CourseRepository


class CourseGetterService:
    def __init__(self, repository: CourseRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
