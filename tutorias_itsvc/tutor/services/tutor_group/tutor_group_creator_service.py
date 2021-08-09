from tutorias_itsvc.tutor.repositories import TutorGroupRepository


class TutorGroupCreatorService:
    def __init__(self, repository: TutorGroupRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        return self.__repository.create(**kwargs)
