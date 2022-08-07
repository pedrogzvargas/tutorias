# -*- coding: utf-8 -*-


from django.core.exceptions import ObjectDoesNotExist
from shared.utils.logger import get_logger

log = get_logger(__file__)


class Repository:

    def __init__(self, model):
        self.__model = model

    def all(self):
        try:
            return self.__model.objects.all()

        except Exception as err:
            log.exception(f'Error {self.__model}, err:{err}')
            raise err

    def filter(self, select_related=[], **fields):
        try:
            return self.__model.objects.select_related(*select_related).filter(**fields)
        except Exception as err:
            log.exception(f'Error {self.__model}, err:{err}')
            raise err

    def get(self, select_related=[], **fields):
        try:
            return self.__model.objects.select_related(*select_related).get(**fields)

        except ObjectDoesNotExist as err:
            return None

        except Exception as err:
            log.exception(f'Error {self.__model}, err:{err}')
            raise err

    def create(self, **fields):
        try:
            return self.__model.objects.create(**fields)

        except Exception as err:
            log.exception(f'Error {self.__model}, err:{err}')
            raise err

    def update(self, id: int, **fields):
        self.__model.objects.filter(pk=id).update(**fields)

    def update_or_create(self, pk_fields: dict, fields: dict):
        try:
            self.__model.objects.update_or_create(**pk_fields, defaults=fields)
        except Exception as err:
            log.exception(f'Error {self.__model}, err:{err}')
            raise err

    def delete(self, id: int):
        try:
            record = self.__model.objects.get(id=id)
            record.delete()
        except Exception as err:
            log.exception(f'Error {self.__model}, err:{err}')
            raise err
