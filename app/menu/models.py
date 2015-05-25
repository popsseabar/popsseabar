from django.db import models


class Section(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


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
    is_active = models.BooleanField(default=True, verbose_name='Active?')
    position = models.PositiveSmallIntegerField('Position')

    class Meta:
        ordering = ['position']

    def __str__(self):
        return self.name
