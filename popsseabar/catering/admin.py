from django.contrib import admin

from ..admin import SingleInstanceAdmin
from .models import Options


admin.site.register(Options, SingleInstanceAdmin)
