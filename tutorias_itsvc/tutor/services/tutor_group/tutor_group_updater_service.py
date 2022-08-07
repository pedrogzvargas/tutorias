from tutorias_itsvc.tutor.repositories import TutorGroupRepository


class TutorGroupUpdaterService:
    def __init__(self, repository: TutorGroupRepository):
        self.__repository = repository

    def __call__(self, id, **kwargs):
        return self.__repository.update(id, **kwargs)
