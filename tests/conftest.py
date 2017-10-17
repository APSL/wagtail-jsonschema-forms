import json
from collections import OrderedDict
import pytest
from model_mommy import mommy
from wagtail.tests.testapp.models import FormPage, FormField
from wagtail.wagtailcore.models import Page


@pytest.mark.django_db()
@pytest.fixture()
def form_page(admin_user):
    root_page = Page.objects.first()
    form = FormPage()
    form.title = "form"
    form.slug = "form"
    form.live = True
    form.owner = admin_user
    root_page.add_child(instance=form)
    form.save()
    return form


@pytest.mark.django_db()
@pytest.fixture()
def singleline(form_page):
    return mommy.make(FormField, page=form_page, field_type="singleline", label="singleline",
                      help_text="singleline", default_value="singleline", required=True)


@pytest.fixture()
def jsonschema_singleline():
    return {
        "type": "string",
        "description": "singleline",
        "maxLength": 150,
        "default": "singleline"
    }


@pytest.mark.django_db()
@pytest.fixture()
def multiline(form_page):
    return mommy.make(FormField, page=form_page, field_type="multiline", label="multiline", default_value="multiline",
                      required=False)


@pytest.fixture()
def jsonschema_multiline():
    return {
        "type": "string",
        "description": "",
        "maxLength": 500,
        "default": "multiline"
    }


@pytest.mark.django_db()
@pytest.fixture()
def date(form_page):
    return mommy.make(FormField, page=form_page, field_type="date", label="date", help_text="date", required=True)


@pytest.fixture()
def jsonschema_date():
    return {
        "type": "string",
        "description": "date",
        "format": "date",
        "default": ""
    }


@pytest.mark.django_db()
@pytest.fixture()
def datetime(form_page):
    return mommy.make(FormField, page=form_page, field_type="datetime", label="datetime", help_text="datetime",
                      required=False)


@pytest.fixture()
def jsonschema_datetime():
    return {
        "type": "string",
        "description": "datetime",
        "format": "date-time",
        "default": ""
    }


@pytest.mark.django_db()
@pytest.fixture()
def email(form_page):
    return mommy.make(FormField, page=form_page, field_type="email", label="email", default_value="email",
                      required=False)


@pytest.fixture()
def jsonschema_email():
    return {
        "type": "string",
        "description": "",
        "maxLength": 100,
        "format": "email",
        "default": "email"
    }


@pytest.mark.django_db()
@pytest.fixture()
def url(form_page):
    return mommy.make(FormField, page=form_page, field_type="url", label="url", required=False)


@pytest.fixture()
def jsonschema_url():
    return {
        "type": "string",
        "description": "",
        "maxLength": 100,
        "format": "uri",
        "default": ""
    }


@pytest.mark.django_db()
@pytest.fixture()
def number(form_page):
    return mommy.make(FormField, page=form_page, field_type="number", label="number", required=True)


@pytest.fixture()
def jsonschema_number():
    return {
        "type": "number",
        "description": "",
        "default": ""
    }


@pytest.mark.django_db()
@pytest.fixture()
def dropdown(form_page):
    return mommy.make(FormField, page=form_page, field_type="dropdown", label="dropdown", help_text="dropdown",
                      choices="dropdown,dropdown2,dropdown3", required=False)


@pytest.fixture()
def jsonschema_dropdown():
    return {
        "type": "string",
        "description": "dropdown",
        "default": "",
        "enum": ["dropdown", "dropdown2", "dropdown3"]
    }


@pytest.mark.django_db()
@pytest.fixture()
def checkbox(form_page):
    return mommy.make(FormField, page=form_page, field_type="checkbox", label="checkbox", required=True)


@pytest.fixture()
def jsonschema_checkbox():
    return {
        "type": "boolean",
        "description": "",
        "default": "",
        "format": "checkbox"
    }


@pytest.mark.django_db()
@pytest.fixture()
def wagtail_form(checkbox, dropdown, number, url, email, datetime, date, multiline, singleline):
    return singleline.page


@pytest.fixture()
def jsonschema_generated(jsonschema_singleline, jsonschema_multiline, jsonschema_date, jsonschema_datetime,
                         jsonschema_email, jsonschema_url, jsonschema_number, jsonschema_dropdown, jsonschema_checkbox):

    properties = OrderedDict()
    properties["checkbox"] = jsonschema_checkbox
    properties["dropdown"] = jsonschema_dropdown
    properties["number"] = jsonschema_number
    properties["url"] = jsonschema_url
    properties["email"] = jsonschema_email
    properties["datetime"] = jsonschema_datetime
    properties["date"] = jsonschema_date
    properties["multiline"] = jsonschema_multiline
    properties["singleline"] = jsonschema_singleline

    json_schema = OrderedDict()
    json_schema["title"] = "form"
    json_schema["type"] = "object"
    json_schema["properties"] = properties
    json_schema["required"] = ["checkbox", "number", "date", "singleline"]
    return json.dumps(json_schema)


########################################################################################################################
# Parser fixtures
########################################################################################################################

@pytest.mark.django_db()
@pytest.fixture()
def single_line(form_page):
    return mommy.make(FormField, page=form_page, field_type="singleline", label="single line",
                      help_text="singleline", default_value="singleline", required=True)


@pytest.mark.django_db()
@pytest.fixture()
def simple_wagtail_form(single_line):
    return single_line.page


@pytest.fixture()
def simple_form_json_correct():
    return {"single line": "Test value"}


@pytest.fixture()
def simple_form_json_incorrect():
    return {"single line": 31351351}


@pytest.fixture()
def json_submited():
    return {"single line": "Test value"}


@pytest.fixture()
def json_ready_to_save():
    return '{"single-line": "Test value"}'
