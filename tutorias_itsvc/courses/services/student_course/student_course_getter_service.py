from tutorias_itsvc.courses.repositories import StudetCourseRepository


class StudetCourseGetterService:
    def __init__(self, repository: StudetCourseRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.get(**kwargs)
