import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'changemepliz'
DEBUG = True
ALLOWED_HOSTS = "*"

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'wagtail.wagtailsites',
    'wagtail.wagtailforms',
    'wagtail.wagtailusers',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailcore',
    'wagtail.contrib.modeladmin',
    'wagtail.tests.testapp',
    'taggit',
    'wagtail_jsonschema_forms'
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'tests.testapp.wsgi.application'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'tests/testapp/wagtail_jsonschema_forms.db',
        'USER': '',
        'PASSWORD': '',
    }
}

WAGTAIL_SITE_NAME = 'Wagtail JsonSchema Test Site'
