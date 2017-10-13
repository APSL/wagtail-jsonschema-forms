from django.db import models
from wagtail.wagtailforms.models import AbstractForm, AbstractEmailForm

from wagtail_jsonschema_forms.mixins import JsonSchemaFormMixin, JsonSchemaEmailFormMixin


class AbstractJsonSchemaForm(JsonSchemaFormMixin, AbstractForm):
    """
    A Form Page that generates a JSON Schema representation of the fields and save it to the model.
    Pages implementing a form that need to generate JSON Schema should inherit from it
    """

    json_schema = models.TextField(help_text=u"Form json Schema representation", blank=True)

    class Meta:
        abstract = True


class AbstractJsonSchemaEmailForm(JsonSchemaEmailFormMixin, AbstractEmailForm):
    """
    A Form Page that generates a JSON Schema representation of the fields and save it to the model. It also send email.
    Pages implementing a form that need to generate JSON Schema and need to send an email should inherit from it
    """

    json_schema = models.TextField(help_text=u"Form json Schema representation", blank=True)

    class Meta:
        abstract = True
