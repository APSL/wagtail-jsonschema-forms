
import json

from wagtail_jsonschema_forms.jsonschema_parser import JsonSchemaParser
from wagtail_jsonschema_forms.jsonschema_generator import JsonSchemaGenerator


class TestJsonschemaParser:

    def test_validate_json_correct(self, simple_form_json_correct, simple_wagtail_form):
        form_schema = JsonSchemaGenerator.wagtail_form_to_json_schema(simple_wagtail_form)
        form_schema = json.loads(form_schema)
        errors = JsonSchemaParser.validate_json(simple_form_json_correct, form_schema)
        assert errors == {}

    def test_validate_json_incorrect(self, simple_form_json_incorrect, simple_wagtail_form):
        form_schema = JsonSchemaGenerator.wagtail_form_to_json_schema(simple_wagtail_form)
        form_schema = json.loads(form_schema)
        errors = JsonSchemaParser.validate_json(simple_form_json_incorrect, form_schema)
        assert "single line" in errors

    def test_prepare_form_data(self, json_submited, json_ready_to_save):
        assert JsonSchemaParser.prepare_form_data(json_submited) == json_ready_to_save

    def test_process_form_submission(self, simple_wagtail_form, json_submited):
        JsonSchemaParser.process_form_submission(simple_wagtail_form, json_submited)
        assert simple_wagtail_form.get_submission_class().objects.all()
