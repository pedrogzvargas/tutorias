from shared.repositories import Repository
from tutorias_itsvc.courses.models import StudetCourse


class StudetCourseRepository(Repository):
    def __init__(self, model=None):
        model = model or StudetCourse
        super(StudetCourseRepository, self).__init__(model)
