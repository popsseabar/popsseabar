from django.forms import ModelForm
from django.forms.models import inlineformset_factory

from ..menu.models import Section, Item


class SectionForm(ModelForm):
    class Meta:
        model = Section
        fields = ['name']

ItemFormSet = inlineformset_factory(Section, Item, fields=('name',
                                                           'description',
                                                           'catering_price',
                                                           'market_price'))
