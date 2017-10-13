#!/usr/bin/env python

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup

setup(
    name='wagtail-jsonschema-forms',
    version='0.1.0',
    description='Generate JsonSchema Forms from Wagtail\'s forms and validate it',
    long_description='Library that allows the generation of a JsonSchema form from a Wagtail\'s form in order '
                     'to use JsonSchema technology. In addition, it allows you to parse the response and validate'
                     ' it. After the validation, the wagtail form is submitted. For example, you can retrieve '
                     'the jsonschema from in an api and then validate the submitted data.',
    author='Carlos Salom',
    author_email='csalom@apsl.net',
    maintainer='Carlos Salom',
    maintainer_email='csalom@apsl.net',
    license='MIT',
    url='https://github.com/APSL/wagtail-jsonschema-forms',
    packages=find_packages(),
    install_requeries=[
        # By default, pick the latest stable version of Django that's officially supported by Wagtail.
        'Django>=1.8.1,<1.12',
        'wagtail>=1.10,<2.0',
        'jsonschema==2.6.0',
        'pytest>=3.1.1',
        'model-mommy>=1.2.6'
    ],
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Operating System :: OS Independent',
        'Topic :: Software Development'
    ]
)
