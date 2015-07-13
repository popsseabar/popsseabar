from .base import *


"""
TOOLBAR CONFIGURATION
"""

INSTALLED_APPS += (
    'debug_toolbar',
)

INTERNAL_IPS = ('127.0.0.1',)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# See: http://django-debug-toolbar.readthedocs.org/en/1.3.2/configuration.html#debug-toolbar-config
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
    'JQUERY_URL': ''
}


"""
CAPTCHA CONFIGURATION
"""

CAPTCHA_TEST_MODE = True


"""
EMAIL CONFIGURATION
"""
# See: https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
