from django.db import models
from simple_history.models import HistoricalRecords


class Phone(models.Model):
    HOME_PHONE = "home_phone"
    MOBILE_PHONE = "mobile_phone"
    PHONE_TYPES = [
        (HOME_PHONE, "Teléfono de Casa"),
        (MOBILE_PHONE, "Teléfono Celular"),
    ]
    number = models.CharField(max_length=25, blank=False)
    type = models.CharField(max_length=15, choices=PHONE_TYPES)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)
    history = HistoricalRecords()

    def __str__(self):
        return self.number

    class Meta:
        default_permissions = ()
        verbose_name = 'Teléfono'
        verbose_name_plural = 'Teléfonos'
        db_table = 'common_phone'


class Gender(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    class Meta:
        default_permissions = ()
        verbose_name = 'Genero'
        verbose_name_plural = 'Generos'
        db_table = 'common_gender'


class State(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

    class Meta:
        default_permissions = ()
        verbose_name = 'Estado'
        verbose_name_plural = 'Estados'
        db_table = 'common_state'


class Disability(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        default_permissions = ()
        verbose_name = 'Deficiencia'
        verbose_name_plural = 'Deficiencias'
        db_table = 'common_disability'


class MaritalStatus(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        default_permissions = ()
        verbose_name = 'Estado civil'
        verbose_name_plural = 'Estados civiles'
        db_table = 'common_marital_status'


class HousingType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        default_permissions = ()
        verbose_name = 'Tipo de vivienda'
        verbose_name_plural = 'Tipos de viviendas'
        db_table = 'common_housing_type'


class HomeStatus(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        default_permissions = ()
        verbose_name = 'Estatus de vivienda'
        verbose_name_plural = 'Estatus de vivienda'
        db_table = 'common_home_status'


class AcademicDegree(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

    class Meta:
        default_permissions = ()
        verbose_name = 'Grado academico'
        verbose_name_plural = 'Grados academicos'
        db_table = 'common_academic_degree'


class Address(models.Model):
    street = models.CharField(max_length=200)
    outdoor_number = models.CharField(max_length=50)
    indoor_number = models.CharField(max_length=50, blank=True, null=True)
    colony = models.CharField(max_length=200)
    locality = models.CharField(max_length=200)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    zip_code = models.CharField(max_length=5)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)

    class Meta:
        default_permissions = ()
        verbose_name = 'Dirección'
        verbose_name_plural = 'Direcciónes'
        db_table = 'common_address'


class Relationship(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    class Meta:
        default_permissions = ()
        verbose_name = 'Relación'
        verbose_name_plural = 'Relaciones'
        db_table = 'common_relationship'


class Attitude(models.Model):
    name = models.CharField(max_length=50, null=True)

    def __str__(self):
        return self.name

    class Meta:
        default_permissions = ()
        verbose_name = 'Actitud'
        verbose_name_plural = 'Actitudes'
        db_table = 'common_attitude'


class Income(models.Model):
    MAIN = "main"
    SECONDARY = "secondary"
    INCOME_TYPES = [
        (MAIN, "Principal"),
        (SECONDARY, "Secundario"),
    ]
    income = models.FloatField()
    type = models.CharField(max_length=20, choices=INCOME_TYPES, default=MAIN)

    class Meta:
        default_permissions = ()
        db_table = 'common_income'


class SchoolCycle(models.Model):
    name = models.CharField(max_length=100, null=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

    class Meta:
        default_permissions = ()
        verbose_name = 'Ciclo escolar'
        verbose_name_plural = 'Ciclos escolares'
        db_table = 'common_school_cycle'
