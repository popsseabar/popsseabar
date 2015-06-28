from django.db import models

from ..models import validate_only_one_instance


class Options(models.Model):
    catering_orders_email = models.EmailField()
    catering_email_confirmation_copy = models.TextField()

    def clean(self):
        validate_only_one_instance(self)

    def __str__(self):
        return 'Options'

    class Meta:
        verbose_name_plural = 'Options'
