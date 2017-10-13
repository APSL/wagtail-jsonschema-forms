from collections import OrderedDict
import json


class JsonSchemaGenerator:

    FIELD_TYPES = {
        "singleline": "generate_singleline",
        "multiline": "generate_multiline",
        "date": "generate_date",
        "datetime": "generate_datetime",
        "email": "generate_email",
        "url": "generate_url",
        "number": "generate_number",
        "dropdown": "generate_dropdown",
        "checkbox": "generate_checkbox",
    }

    @staticmethod
    def generate_singleline(field):
        return {
            "type": "string",
            "description": field.help_text,
            "maxLength": 150,
            "default": field.default_value
        }

    @staticmethod
    def generate_multiline(field):
        return {
            "type": "string",
            "description": field.help_text,
            "maxLength": 500,
            "default": field.default_value
        }

    @staticmethod
    def generate_email(field):
        return {
            "type": "string",
            "description": field.help_text,
            "maxLength": 100,
            "format": "email",
            "default": field.default_value
        }

    @staticmethod
    def generate_date(field):
        return {
            "type": "string",
            "description": field.help_text,
            "format": "date",
            "default": field.default_value
        }

    @staticmethod
    def generate_datetime(field):
        return {
            "type": "string",
            "description": field.help_text,
            "format": "date-time",
            "default": field.default_value
        }

    @staticmethod
    def generate_url(field):
        return {
            "type": "string",
            "description": field.help_text,
            "maxLength": 100,
            "format": "uri",
            "default": field.default_value
        }

    @staticmethod
    def generate_number(field):
        return {
            "type": "number",
            "description": field.help_text,
            "default": field.default_value
        }

    @staticmethod
    def generate_dropdown(field):
        return {
            "type": "string",
            "description": field.help_text,
            "default": field.default_value,
            "enum": field.choices.split(",")
        }

    @staticmethod
    def generate_checkbox(field):
        return {
            "type": "boolean",
            "description": field.help_text,
            "default": field.default_value,
            "format": "checkbox"
        }

    @staticmethod
    def wagtail_form_to_json_schema(form):
        """
        This function expects a wagtail form and return a Json Schema representation
        :param form: wagtail form
        :return: dict
        """
        json_schema = OrderedDict()
        json_schema["title"] = form.slug
        json_schema["type"] = "object"

        properties = OrderedDict()
        required = []
        for field in form.form_fields.all():
            field_type = field.field_type
            if field_type in JsonSchemaGenerator.FIELD_TYPES:
                properties[field.label] = getattr(JsonSchemaGenerator,
                                                  JsonSchemaGenerator.FIELD_TYPES[field_type])(field)

                if field.required:
                    required.append(field.label)

        json_schema["properties"] = properties
        json_schema["required"] = required
        return json.dumps(json_schema)
