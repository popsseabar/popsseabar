from django.forms import Form, CharField, ChoiceField, \
    EmailField, IntegerField, TypedChoiceField


class CateringForm(Form):
    qty = TypedChoiceField(
        choices=((str(x), x) for x in range(0, 11)),
        coerce=int,
        initial='0',
        required=False)


class ContactForm(Form):
    ZIP_ERROR = 'Enter a valid 5 digit zip code.'

    name = CharField()
    business_name = CharField(required=False)
    email = EmailField()
    address1 = CharField(label='Address')
    address2 = CharField(label='Address 2', required=False)
    city = CharField(initial='Washington')
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
