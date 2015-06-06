from django.db import models
from django.core.exceptions import ValidationError


def validate_only_one_instance(obj):
    """
    Throw ValidationError if you try to save more than one instance
    See: http://stackoverflow.com/a/6436008
    """
    model = obj.__class__
    if (model.objects.count() > 0 and
            obj.id != model.objects.get().id):
        raise ValidationError(
            'Can only create 1 instance of {}.'.format(model.__name__))


class Options(models.Model):
    our_story_copy = models.TextField()
    address = models.TextField()
    hours = models.TextField()
    delivery_url = models.CharField(max_length=200)
    gift_certificates_url = models.CharField(max_length=200)
    email_signup_url = models.CharField(max_length=200)

    def clean(self):
        validate_only_one_instance(self)

    def __str__(self):
        return 'Options'

    class Meta:
        verbose_name_plural = 'Options'
