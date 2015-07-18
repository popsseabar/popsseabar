from .base import *


"""
COMPRESSION CONFIGURATION
"""
LIBSASS_SOURCE_COMMENTS = False
LIBSASS_OUTPUT_STYLE = 'compressed'


"""
STATIC FILE CONFIGURATION
"""

# See: https://warehouse.python.org/project/whitenoise/
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'


"""
DJANGO STORAGES
"""
# See: http://django-storages.readthedocs.org/en/latest/backends/amazon-S3.html
INSTALLED_APPS += (
    'storages',
)

DEFAULT_FILE_STORAGE = 'popsseabar.MediaRootS3BotoStorage'

AWS_ACCESS_KEY_ID = environ.get('AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = environ.get('AWS_SECRET_ACCESS_KEY')
AWS_STORAGE_BUCKET_NAME = environ.get('AWS_STORAGE_BUCKET_NAME')
AWS_S3_CUSTOM_DOMAIN = environ.get('AWS_S3_CUSTOM_DOMAIN')
AWS_QUERYSTRING_AUTH = False


"""
EMAIL CONFIGURATION
"""
# See: https://github.com/django-ses/django-ses
EMAIL_BACKEND = 'django_ses.SESBackend'

# AWS_SES_REGION_NAME = environ.get('AWS_SES_REGION_NAME')
# AWS_SES_REGION_ENDPOINT = environ.get('AWS_SES_REGION_ENDPOINT')
AWS_SES_RETURN_PATH = environ.get('AWS_SES_RETURN_PATH')
