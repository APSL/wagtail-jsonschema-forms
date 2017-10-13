
from wagtail_jsonschema_forms.jsonschema_generator import JsonSchemaGenerator


class TestJsonschemaGenerator:

    def test_singleline_generator(self, singleline, jsonschema_singleline):
        assert JsonSchemaGenerator.generate_singleline(singleline) == jsonschema_singleline

    def test_multiline_generator(self, multiline, jsonschema_multiline):
        assert JsonSchemaGenerator.generate_multiline(multiline) == jsonschema_multiline

    def test_date_generator(self, date, jsonschema_date):
        assert JsonSchemaGenerator.generate_date(date) == jsonschema_date

    def test_datetime_generator(self, datetime, jsonschema_datetime):
        assert JsonSchemaGenerator.generate_datetime(datetime) == jsonschema_datetime

    def test_email_generator(self, email, jsonschema_email):
        assert JsonSchemaGenerator.generate_email(email) == jsonschema_email

    def test_url_generator(self, url, jsonschema_url):
        assert JsonSchemaGenerator.generate_url(url) == jsonschema_url

    def test_number_generator(self, number, jsonschema_number):
        assert JsonSchemaGenerator.generate_number(number) == jsonschema_number

    def test_dropdown_generator(self, dropdown, jsonschema_dropdown):
        assert JsonSchemaGenerator.generate_dropdown(dropdown) == jsonschema_dropdown

    def test_checkbox_generator(self, checkbox, jsonschema_checkbox):
        assert JsonSchemaGenerator.generate_checkbox(checkbox) == jsonschema_checkbox

    def test_schemajson_generator(self, wagtail_form, jsonschema_generated):
        assert JsonSchemaGenerator.wagtail_form_to_json_schema(wagtail_form) == jsonschema_generated
