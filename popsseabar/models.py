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
