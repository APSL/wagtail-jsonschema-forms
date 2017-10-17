import os
import re
import codecs

try:
    from setuptools import setup, find_packages
except ImportError:
    from distutils.core import setup


def get_version(package):
    """
    Return package version as listed in `__version__` in `init.py`.
    """
    init_py = codecs.open(os.path.join(package, '__init__.py'), encoding='utf-8').read()
    return re.search("^__version__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)


def get_author(package):
    """
    Return package author as listed in `__author__` in `init.py`.
    """
    init_py = codecs.open(os.path.join(package, '__init__.py'), encoding='utf-8').read()
    return re.search("^__author__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)


def get_email(package):
    """
    Return package email as listed in `__email__` in `init.py`.
    """
    init_py = codecs.open(os.path.join(package, '__init__.py'), encoding='utf-8').read()
    return re.search("^__email__ = ['\"]([^'\"]+)['\"]", init_py, re.MULTILINE).group(1)

setup(
    name='wagtail-jsonschema-forms',
    version=get_version('wagtail_jsonschema_forms'),
    description='Generate JsonSchema Forms from Wagtail\'s forms and validate it',
    long_description='Library that allows the generation of a JsonSchema form from a Wagtail\'s form in order '
                     'to use JsonSchema technology. In addition, it allows you to parse the response and validate'
                     ' it. After the validation, the wagtail form is submitted. For example, you can retrieve '
                     'the jsonschema from in an api and then validate the submitted data.',
    author=get_author('wagtail_jsonschema_forms'),
    author_email=get_email('wagtail_jsonschema_forms'),
    maintainer=get_author('wagtail_jsonschema_forms'),
    maintainer_email=get_email('wagtail_jsonschema_forms'),
    license='MIT',
    url='https://github.com/APSL/wagtail-jsonschema-forms',
    packages=find_packages(),
    install_requires=[
        # By default, pick the latest stable version of Django that's officially supported by Wagtail.
        'Django>=1.8.1,<1.12',
        'wagtail>=1.10,<2.0',
        'jsonschema==2.6.0',
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
