from django.db.models import Model
from django.forms.models import model_to_dict


class ModelPopulate:
    @staticmethod
    def populate(model: Model, values: dict):
        for attr, value in values.items():
            if hasattr(model, attr):
                setattr(model, attr, value)
        return model

    @staticmethod
    def populate_as_dict(model: Model, values: dict):
        model_object = model()
        populated_dict = dict()
        for attr, value in values.items():
            if hasattr(model_object, attr):
                populated_dict[f'{attr}'] = value
        return populated_dict

    @staticmethod
    def model_as_dict(model: Model):
        model_dict = model_to_dict(model)
        return model_dict

