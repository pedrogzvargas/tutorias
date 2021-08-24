from tutorias_itsvc.tutor.repositories import TutorSubjectRepository


class TutorSubjectFilterService:
    def __init__(self, repository: TutorSubjectRepository):
        self.__repository = repository

    def __call__(self, **kwargs):
        select_related = ["tutor", "subject", "school_cycle"]
        return self.__repository.filter(select_related=select_related, **kwargs)
