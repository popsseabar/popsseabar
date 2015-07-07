from django.db import models

from sorl.thumbnail import ImageField

from ..models import validate_only_one_instance


class Section(models.Model):
    name = models.CharField(max_length=200)
    position = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        model = self.__class__

        if self.position is None:
            # Append
            try:
                last = model.objects.order_by('-position')[0]
                self.position = last.position + 1
            except IndexError:
                # First row
                self.position = 0

        return super(Section, self).save(*args, **kwargs)


class Item(models.Model):
    section = models.ForeignKey(Section)
    name = models.CharField(max_length=200)
    description = models.CharField(
        max_length=200,
        blank=True)
    price = models.DecimalField(
        decimal_places=2,
        max_digits=5)
    catering_price = models.DecimalField(
        decimal_places=2,
        max_digits=5,
        verbose_name='Catering Price')
    market_price = models.BooleanField(default=False, verbose_name='Market Price')
    is_active = models.BooleanField(default=True, verbose_name='Menu?')
    catering_active = models.BooleanField(default=True, verbose_name='Catering?')
    position = models.PositiveSmallIntegerField()

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.name


class Image(models.Model):
    url = ImageField(upload_to='',
                     height_field='height',
                     width_field='width',
                     verbose_name='Menu')
    height = models.PositiveIntegerField(editable=False)
    width = models.PositiveIntegerField(editable=False)

    def clean(self):
        validate_only_one_instance(self)

    def __str__(self):
        return 'Menu'
