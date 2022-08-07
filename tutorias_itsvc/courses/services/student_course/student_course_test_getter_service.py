from tutorias_itsvc.courses.repositories import StudetCourseRepository


class StudentCourseGetterService:
    def __init__(self, repository: StudetCourseRepository):
        self.__repository = repository

    def __call__(self, student_id, course_id):
        student_course = self.__repository.get(student_id=student_id, course_id=course_id)
        return self.__repository.get()
