Wagtail JsonSchema Forms
========================

.. image:: https://api.travis-ci.org/APSL/wagtail-jsonschema-forms.svg?branch=master
    :target: https://travis-ci.org/APSL/wagtail-jsonschema-forms

Wagtail JsonSchema Forms is a simple Django app to Generate JsonSchema Forms from Wagtail's forms and validate it.

This app allows the generation of a JsonSchema form from a Wagtail's form in order to use JsonSchema technology.
In addition, it allows you to parse the response and validate it. After the validation, the wagtail form is
submitted.

For example, you can retrieve the jsonschema from through an api, then validate the submitted data and finally
submit de wagtail form.

Installation
------------

You can install "wagtail_jsonschema_forms" via `pip`_ from `APSL GitHub`_:

* pip install git+https://github.com/APSL/wagtail_jsonschema_forms.git#egg=wagtail_jsonschema_forms

And then you have to add :code:`wagtail_jsonschema_forms` to your :code:`INSTALLED_APPS`.


Utilities provided
------------------
This app offers two python classes to generate the jsonschema and to submit the json response.

JsonSchemaGenerator
~~~~~~~~~~~~~~~~~~~

This first class has a method :code:`wagtail_form_to_json_schema` that goes over
all the fields of the form and generate its jsonschema representation, if they are suported.

Every suported field type has a method that generate the representation, which is called during the generation.
If the field is required, it will be indicated too.


JsonSchemaParser
~~~~~~~~~~~~~~~~

This second class provides two main methods:

* :code:`validate_json`:
    method that validates the json recieved under the schema a return a dict with the possible errors.
    If there are no error, a empty dict will be returned.
* :code:`process_form_submission`:
    method that accepts form instance with submitted data and page and creates submission instance.
    Inside of this method, another one is called to format the data submited in order to create the
    submission instance.


Usage
-----
As was explained before, this django app generates jsonschema forms from Wagtail's form and validate it.
Wagtail's forms offers a very rich set of form field types. However, not all of them are suported on
JsonSchema and has not been covered on this app. For that reason, when you declare your :code:`FormField`
class on your models.py you should override the field_type field and the :code:`FORM_FIELD_CHOICES` variable:

.. code-block:: python

    FORM_FIELD_CHOICES = (
        ('singleline', _('Single line text')),
        ('multiline', _('Multi-line text')),
        ('email', _('Email')),
        ('number', _('Number')),
        ('url', _('URL')),
        ('checkbox', _('Checkbox')),
        ('dropdown', _('Drop down')),
        ('date', _('Date')),
        ('datetime', _('Date/time')),
      )

    field_type = models.CharField(verbose_name=_('field type'), max_length=16, choices=FORM_FIELD_CHOICES)

There are two ways to use wagtail_json_schema_forms: you can choose between using the mixins or the abstract
models provided.

Mixins
~~~~~~

If you choose to use the mixins, the first thing thant you have to do is to add a new :code:`TextField` atribute
to your wagtail form page called 'json_schema'. This field will be used to save the JsonSchema representation
of the form.

Two mixins are provided: :code:`JsonSchemaFormMixin` and :code:`JsonSchemaEmailFormMixin`, which inherit from the first one.

:code:`JsonSchemaFormMixin` overrides the save method in order to generate the json schema before every time the
wagtail page is saved. This mixin uses the generator class explained above to prepare the jsonschema from the form.

It's also overrided the method :code:`process_form_submission`, where it's checked if the form has been submited as
a usual wagtail form or using jsonschema. If jsonschema has been used for submition, the parser class is used
to register the form submission.

As said, the :code:`JsonSchemaEmailFormMixin` inherits from :code:`JsonSchemaFormMixin`. The diference between them is in
the process of the form submission. This second mixin tries to send an email after the form submission, if the
:code:`to_address` attribute of the wagtail page has been filed.


Abstract Models
~~~~~~~~~~~~~~~

Again, there are two abstract models provided to allow to add the jsonschema functionality to a plain WagtailForm
and a EmailWagtailForm: :code:`AbstractJsonSchemaForm` and :code:`AbstractJsonSchemaEmailForm`.

These abstract models inherit from the mixins explained above and the :code:`AbstractForm` or :code:`AbstractEmailForm`.
They also add the new :code:`TextField` atribute required. Then, Wagtail Pages implementing a form that need to
generate a JsonSchema (and to send and email) should inherit from it.



Contributing
------------

Contributions are very welcome. Please open a pull request or `file an issue`_.
Tests will be ready as soon as posible, please ensure the coverage at least stays the same
before you submit a pull request.

License
-------

Distributed under the terms of the `MIT`_ license, "wagtail_jsonschema_forms" is free and open source software


Issues
------

If you encounter any problems, please `file an issue`_ along with a detailed description.

.. _`pip`: https://pypi.python.org/pypi/pip/
.. _`APSL GitHub`: https://github.com/APSL/wagtail_jsonschema_forms
.. _`file an issue`: https://github.com/APSL/wagtail_jsonschema_forms/issues
.. _`MIT`: http://opensource.org/licenses/MIT