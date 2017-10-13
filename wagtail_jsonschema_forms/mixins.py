
from wagtail.wagtailadmin.utils import send_mail
from wagtail_jsonschema_forms.jsonschema_generator import JsonSchemaGenerator
from wagtail_jsonschema_forms.jsonschema_parser import JsonSchemaParser


class JsonSchemaFormMixin:

    def save(self, *args, **kwargs):
        self.json_schema = self.generate_json_schema()
        super().save(*args, **kwargs)

    def generate_json_schema(self):
        """
        Function that generates the json schema representation of the form
        """
        return JsonSchemaGenerator.wagtail_form_to_json_schema(self)

    def process_form_submission(self, form):
        """
        Function that check the way that the form has been submited
        :param form: WagtailForm or dict
        :return:
        """
        if hasattr(form, "data"):
            super().process_form_submission(form)
        else:
            self.process_json_form_submission(form)

    def process_json_form_submission(self, json_submited):
        """
        Function that process json form submission
        :param json_submited: dict
        :return:
        """
        JsonSchemaParser.process_form_submission(self, json_submited)


class JsonSchemaEmailFormMixin(JsonSchemaFormMixin):

    def process_json_form_submission(self, json_submited):
        """
        Function that process json form submission and send an email from a json representation of the submitted data
        :param json_submited: dict
        :return:
        """
        JsonSchemaParser.process_form_submission(self, json_submited)
        self.send_mail_from_json(json_submited)

    def send_mail_from_json(self, form_fields):
        """
        Function that send a email from a json representation of the post data of the form.
        Based on wagtail.wagtailforms.models.AbstractEmailForm.send_mail
        :param form_fields: dict
        :return:
        """
        if self.to_address:
            addresses = [x.strip() for x in self.to_address.split(',')]
            content = []
            for field_key, value in form_fields.items():
                if isinstance(value, list):
                    value = ', '.join(value)
                content.append('{}: {}'.format(field_key.capitalize(), value))
            content = '\n'.join(content)
            send_mail(self.subject, content, addresses, self.from_address)
