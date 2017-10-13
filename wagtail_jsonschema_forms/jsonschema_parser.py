
from django.core.serializers.json import DjangoJSONEncoder
from django.utils.six import text_type
from django.utils.text import slugify

import json
from jsonschema.validators import validator_for
from unidecode import unidecode


class JsonSchemaParser:

    @staticmethod
    def validate_json(json_form, schema, *args, **kwargs):
        """
        Function that validates the json recieved under the schema and returns a dict with the errors, if there are any
        :param json_form: dict
        :param schema: dict
        :return dict
        """
        cls = validator_for(schema)
        cls.check_schema(schema)
        json_errors = cls(schema, *args, **kwargs).iter_errors(json_form)
        errors = {}
        for error in json_errors:
            # errors can be from fields validation or required camps
            form_field = error.path[0] if error.path else error.validator_value[0]
            errors[form_field] = error.message
        return errors

    @staticmethod
    def process_form_submission(form, json_submited):
        """
        Function that accepts form instance with submitted data and page and creates submission instance.
        :param form: Form Page
        :param json_submited: str
        """
        form.get_submission_class().objects.create(form_data=JsonSchemaParser.prepare_form_data(json_submited),
                                                   page=form)

    @staticmethod
    def prepare_form_data(json_submited):
        """
        Function that prepare json field keys to the submition
        :param json_submited: dict
        :return str
        """
        form_data = {}
        for field_key, value in json_submited.items():
            # same conversion as clean_name in wagtail.wagtailforms.models.AbstractFormField
            form_data[str(slugify(text_type(unidecode(field_key))))] = value
        return json.dumps(form_data, cls=DjangoJSONEncoder)
