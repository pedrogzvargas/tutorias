from tutorias_itsvc.users.services.personal_information import PersonalInformationGetterService
from tutorias_itsvc.users.services.personal_information import PersonalInformationCreatorService
from tutorias_itsvc.users.repositories import PersonalInformationRepository
from tutorias_itsvc.students.services.phone import PhoneFilterService
from tutorias_itsvc.students.services.phone import PhoneCreatorService
from tutorias_itsvc.students.repositories import StudentRepository
from tutorias_itsvc.students.services.student_getter_service import StudentGetterService
from tutorias_itsvc.students.repositories import StudentPhoneRepository


class GeneralInformationCreatorService:
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

    def get_personal_information(self):
        repository = PersonalInformationRepository()
        personal_information_getter_service = PersonalInformationGetterService(repository)
        personal_information = personal_information_getter_service(user_id=self.__user_id)
        return personal_information

    def create_phones(self, **kwargs):
        repository = StudentPhoneRepository()
        phone_creator_service = PhoneCreatorService(repository)
        mobile_phone, home_phone = self.get_phones()
        if not mobile_phone or mobile_phone != kwargs.get('mobile_phone'):
            mobile_phone_values = dict(
                student_id=self.__student.id,
                number=kwargs.get('mobile_phone'),
                type='mobile_phone'
            )
            phone_creator_service(**mobile_phone_values)
        if not home_phone or home_phone != kwargs.get('home_phone'):
            home_phone_values = dict(
                student_id=self.__student.id,
                number=kwargs.get('home_phone'),
                type='home_phone'
            )
            phone_creator_service(**home_phone_values)

    def create_personal_information(self, **kwargs):
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
        personal_information_creator_service = PersonalInformationCreatorService(repository)
        personal_information_creator_service(**personal_information_values)

    def get_phones(self):
        mobile_phone = None
        home_phone = None
        repository = StudentPhoneRepository()
        phone_filter_service = PhoneFilterService(repository)
        current_mobile_phone = phone_filter_service(student__user_id=self.__user_id, type='mobile_phone').first()
        current_home_phone = phone_filter_service(student__user_id=self.__user_id, type='home_phone').first()
        if current_mobile_phone:
            mobile_phone = current_mobile_phone.number
        if current_home_phone:
            home_phone = current_home_phone.number
        return mobile_phone, home_phone

    def __call__(self, **kwargs):
        personal_information = self.get_personal_information()
        if personal_information:
            raise Exception("Ya exsite un registro para este usuario")
        self.create_personal_information(**kwargs)
        self.create_phones(**kwargs)
