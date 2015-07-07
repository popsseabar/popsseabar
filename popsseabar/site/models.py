from django.db import models

from ..models import validate_only_one_instance


class Options(models.Model):
    our_story_copy = models.TextField()
    address = models.TextField()
    hours = models.TextField()
    delivery_url = models.CharField(max_length=200)
    gift_certificates_url = models.CharField(max_length=200)
    email_signup_url = models.CharField(max_length=200)
    alert_copy = models.TextField(blank=True)

    def clean(self):
        validate_only_one_instance(self)

    def __str__(self):
        return 'Options'

    class Meta:
        verbose_name_plural = 'Options'
