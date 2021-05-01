from tutorias_itsvc.users.services.personal_information import PersonalInformationGetterService
from tutorias_itsvc.users.repositories import PersonalInformationRepository
from tutorias_itsvc.students.services.phone import PhoneFilterService
from tutorias_itsvc.students.repositories import StudentPhoneRepository


class GeneralInformationGetterService:
    def __init__(self, user_id):
        self.__user_id = user_id

    def get_personal_information(self):
        repository = PersonalInformationRepository()
        personal_information_getter_service = PersonalInformationGetterService(repository)
        personal_information = personal_information_getter_service(user_id=self.__user_id)
        return personal_information

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

    def __call__(self):
        general_information = dict()
        personal_information = self.get_personal_information()
        mobile_phone, home_phone = self.get_phones()
        if personal_information:
            general_information = dict(
                email=personal_information.user.email,
                mobile_phone=mobile_phone,
                home_phone=home_phone,
                birth_date=personal_information.birth_date,
                place_birth=personal_information.place_birth,
                gender_id=personal_information.gender_id,
                marital_status_id=personal_information.marital_status_id,
                marital_status_description=personal_information.marital_status_description,
                has_children=personal_information.has_children,
                number_of_children=personal_information.number_of_children,
                height=personal_information.height,
                weight=personal_information.weight,
            )
        return general_information
