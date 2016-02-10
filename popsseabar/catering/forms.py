import time

from django.core.validators import RegexValidator
from django.forms import Form, CharField, ChoiceField, \
    DateField, DateInput, EmailField, EmailInput, IntegerField, \
    TextInput, TypedChoiceField
from django.forms.widgets import Textarea

from captcha.fields import CaptchaField


class CateringForm(Form):
    qty = TypedChoiceField(
        choices=((str(x), x) for x in range(0, 11)),
        coerce=int,
        initial='0',
        required=False)


class ContactForm(Form):
    error_css_class = 'error'
    required_css_class = 'required'

    ZIP_ERROR = 'Enter a valid 5 digit zip code.'

    name = CharField(widget=TextInput(attrs={'placeholder': 'Justin Doe'}))
    business_name = CharField(required=False)
    phone = CharField(
        widget=TextInput(attrs={'placeholder': '202-534-3933'}),
        validators=[
            RegexValidator(
                r'(\d{3})\D*(\d{3})\D*(\d{4})\D*(\d*)$',
                'Enter a valid 10 digit phone number.',
                'Invalid Phone Number'
            ),
        ]
    )
    email = EmailField(widget=EmailInput(attrs={'placeholder': 'justin@example.com'}))
    address1 = CharField(label='Address',
        widget=TextInput(attrs={'placeholder': '1817 Columbia Road NW'}))
    address2 = CharField(label='Address 2', required=False)
    city = CharField(widget=TextInput(attrs={'placeholder': 'Washington'}))
    state = ChoiceField(
        choices=(('DC', 'District of Columbia'),
                 ('MD', 'Maryland'),
                 ('VA', 'Virginia')),
        initial='DC')
    zip_code = IntegerField(
        min_value=0,
        max_value=99999,
        required=False,
        error_messages={
            'invalid': ZIP_ERROR,
            'min_value': ZIP_ERROR,
            'max_value': ZIP_ERROR,
        })
    catering_date = DateField(widget=DateInput(attrs={'class': 'datepicker',
                                                      'placeholder': time.strftime("%m/%d/%Y")},
                                               format='%m/%d/%Y'))
    notes = CharField(required=False, widget=Textarea())
    captcha = CaptchaField()
