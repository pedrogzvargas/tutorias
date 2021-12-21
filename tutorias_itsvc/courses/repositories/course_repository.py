from shared.repositories import Repository
from tutorias_itsvc.courses.models import Course


class CourseRepository(Repository):
    def __init__(self, model=None):
        model = model or Course
        super(CourseRepository, self).__init__(model)
