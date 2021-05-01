from django.contrib.auth.models import AbstractUser, models
from django.db.models import CharField
from django.urls import reverse
from django.utils.translation import gettext_lazy as _

from tutorias_itsvc.common.models import (
    AcademicDegree,
    MaritalStatus,
    Gender,
    Disability,
    Phone,
    Attitude,
    Relationship
)


class User(AbstractUser):
    """Default user for tutorias_itsvc."""

    #: First and last name do not cover name patterns around the globe
    second_name = CharField(_("Second Name of User"), blank=True, max_length=255)
    second_last_name = CharField(_("Second Last Name of User"), blank=True, max_length=255)

    def get_absolute_url(self):
        """Get url for user's detail view.

        Returns:
            str: URL for user detail.

        """
        return reverse("users:detail", kwargs={"username": self.username})


class PersonalInformation(models.Model):
    user = models.OneToOneField(User, related_name='personal_information', on_delete=models.CASCADE)
    place_birth = models.CharField(max_length=255, null=True, blank=True)
    birth_date = models.DateField(null=True, blank=True)
    has_children = models.BooleanField(null=True, blank=True, default=None)
    number_of_children = models.IntegerField(null=True, blank=True, default=None)
    gender = models.ForeignKey(Gender, related_name='gender', null=True, blank=True, on_delete=models.CASCADE)
    marital_status = models.ForeignKey(MaritalStatus, on_delete=models.CASCADE)
    marital_status_description = models.TextField(null=True, blank=True)
    height = models.FloatField(null=True, blank=True)
    weight = models.FloatField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)


class Person(models.Model):
    first_name = models.CharField(max_length=100)
    second_name = models.CharField(max_length=100, null=True, blank=True)
    last_name = models.CharField(max_length=100)
    second_last_name = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        default_permissions = ()
        db_table = "users_person"
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'


class PersonPhone(Phone):
    person = models.ForeignKey(Person, related_name='phones', on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=1)

    class Meta:
        default_permissions = ()
        db_table = "users_person_phone"
        verbose_name = 'Teléfono de persona'
        verbose_name_plural = 'Teléfonos de personas'


class Sibling(Person):
    gender = models.ForeignKey(Gender, null=True, blank=True, on_delete=models.CASCADE)
    birth_date = models.DateField(null=True, blank=True)
    academic_degree = models.ForeignKey(AcademicDegree, on_delete=models.CASCADE)
    relationship = models.ForeignKey(Relationship, null=True, on_delete=models.CASCADE)
    attitude = models.ForeignKey(Attitude, null=True, on_delete=models.CASCADE)

    class Meta:
        default_permissions = ()
        db_table = "users_sibling"
        verbose_name = 'Hermano'
        verbose_name_plural = 'Hermanos'


class EmergencyContact(Person):
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    class Meta:
        default_permissions = ()


class Manager(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        default_permissions = ()


class Coordinator(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        default_permissions = ()


class Academic(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        default_permissions = ()


class Psychologist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        default_permissions = ()


class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        default_permissions = ()


class ProfileImage(models.Model):
    user = models.ForeignKey(User, related_name='profile_picture', on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_picture', max_length=255)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    class Meta:
        default_permissions = ()
        db_table = "users_profile_image"
