from tutorias_itsvc.users.services.personal_information import PersonalInformationUpdaterService
from tutorias_itsvc.users.repositories import PersonalInformationRepository
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.services.student_getter_service import StudentGetterService
from .general_information_creator_service import GeneralInformationCreatorService


class GeneralInformationUpdaterService:
    def __init__(self, user_id):
        self.__user_id = user_id
        self.__student = None
        self.setup()

    def setup(self):
        repository = StudentRepository()
        student_getter_service = StudentGetterService(repository)
        self.__student = student_getter_service(user_id=self.__user_id)
        if not self.__student:
            raise Exception("Invalid student")

    def update_personal_information(self, id, **kwargs):
        personal_information_values = dict(
            user_id=self.__user_id,
            birth_date=kwargs.get('birth_date'),
            place_birth=kwargs.get('place_birth'),
            gender_id=kwargs.get('gender_id'),
            marital_status_id=kwargs.get('marital_status_id'),
            marital_status_description=kwargs.get('marital_status_description'),
            has_children=kwargs.get('has_children'),
            number_of_children=kwargs.get('number_of_children'),
            height=kwargs.get('height'),
            weight=kwargs.get('weight')
        )
        repository = PersonalInformationRepository()
        personal_information_updater_service = PersonalInformationUpdaterService(repository)
        personal_information_updater_service(id, **personal_information_values)

    def __call__(self, **kwargs):
        creator_service = GeneralInformationCreatorService(self.__user_id)
        personal_information = creator_service.get_personal_information()
        if not personal_information:
            raise Exception("No existe un estudiante con este id")
        self.update_personal_information(personal_information.id, **kwargs)
        # self.create_phones(**kwargs)
