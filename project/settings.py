from __future__ import unicode_literals

import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = ')0!1=11x(7m6b@m8ht_&xump=#)xi@-1l!7ee4lwhjoch=cny$'
DEBUG = True
ALLOWED_HOSTS = []
LANGUAGE_CODE = 'de'
LANGUAGES = (
    ('de', 'Deutsch'),
)
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True
STATIC_URL = '/static/'
SITE_ID = 1
INSTALLED_APPS = [
    'project',
    'cms',
    'menus',
    'sekizai',
    'treebeard',
    'djangocms_admin_style',
    'django.contrib.redirects',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
]
MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'cms.middleware.page.CurrentPageMiddleware',
    'cms.middleware.user.CurrentUserMiddleware',
    'cms.middleware.toolbar.ToolbarMiddleware',
    'cms.middleware.utils.ApphookReloadMiddleware',
    'cms.middleware.language.LanguageCookieMiddleware',
]
ROOT_URLCONF = 'project.urls'
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'sekizai.context_processors.sekizai',
                'django.template.context_processors.static',
                'cms.context_processors.cms_settings'
            ],
        },
    },
]
WSGI_APPLICATION = 'project.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


CMS_TEMPLATES = (
    ('cms/standard.html', 'standard'),
)
CMS_CACHE_DURATIONS = {
    'content': 0,
    'menus': 0,
    'permissions': 0,
}
CMS_LANGUAGES = {
    1: [
        {
            'code': 'de',
            'name': 'Deutsch',
            'fallbacks': ['en'],
        },
    ],
    'default': {
        'fallbacks': ['de',],
        'redirect_on_fallback': True,
        'public': True,
        'hide_untranslated': True,
    },
}
CMS_MENU_TITLE_OVERWRITE = True
CMS_PERMISSION = False
CMS_REDIRECTS = True
CMS_URL_OVERWRITE = False
