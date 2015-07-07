import importlib
import logging
from os import environ

from django.core.mail import send_mail
from django.forms.models import formset_factory
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.views.generic import FormView

from ..menu.models import Item
from .forms import CateringForm, ContactForm
from .models import Options


settings_module = environ.get('DJANGO_SETTINGS_MODULE')
settings = importlib.import_module(settings_module)

logger = logging.getLogger('popsseabar')


class CateringView(FormView):
    template_name = 'catering/index.html'
    form_class = CateringForm
    success_url = 'success/'

    def get(self, request):
        """
        Handles GET requests and instantiates blank versions of the form
        and its inline formsets.
        """

        catering_items = Item.objects.filter(catering_active=True)\
                             .order_by('section', 'position')
        CateringFormSet = formset_factory(CateringForm, extra=catering_items.count())
        catering_formset = CateringFormSet(prefix='catering')
        catering_items_and_formset = zip(catering_items, catering_formset)

        contact_form = ContactForm(prefix='contact')

        return self.render_to_response(
            self.get_context_data(catering_items=catering_items,
                                  catering_formset=catering_formset,
                                  catering_items_and_formset=catering_items_and_formset,
                                  contact_form=contact_form))

    def post(self, request, *args, **kwargs):
        """
        Handles POST requests, instantiating a form instance with the passed
        POST variables and then checked for validity.
        """

        # check if options exist, if not throw a 500 error
        try:
            options = Options.objects.all().order_by('pk').reverse()[0]
        except IndexError:
            raise Exception('Catering options not defined')

        catering_items = Item.objects.filter(catering_active=True)\
                             .order_by('section', 'position')
        CateringFormSet = formset_factory(CateringForm)
        catering_formset = CateringFormSet(data=request.POST, prefix='catering')
        contact_form = ContactForm(data=request.POST, prefix='contact')

        if catering_formset.is_valid() and contact_form.is_valid():
            cleaned_catering_items_and_formset = zip(
                catering_items,
                catering_formset.cleaned_data)
            cleaned_contact_form = contact_form.cleaned_data

            message_context = {}
            message_context['contact_form'] = cleaned_contact_form
            message_context['catering_items_and_formset'] = \
                cleaned_catering_items_and_formset
            order_message = render_to_string(
                'catering/email.txt', message_context)

            # TODO: move trimming to the model
            message_context['catering_email_confirmation_copy'] = \
                options.catering_email_confirmation_copy.strip()
            confirmation_message = render_to_string(
                'catering/email.txt', message_context)

            send_mail(
                from_email=getattr(settings, 'SERVER_EMAIL'),
                recipient_list=[options.catering_orders_email],
                subject='Pop\'s SeaBar Catering Order Received',
                message=order_message)

            send_mail(
                from_email=getattr(settings, 'SERVER_EMAIL'),
                recipient_list=[cleaned_contact_form['email']],
                subject='Pop\'s SeaBar Catering Order Confirmation',
                message=confirmation_message)

            return HttpResponseRedirect(self.get_success_url())

        else:
            logger.debug('---------> Form is NOT valid')
            catering_items_and_formset = zip(catering_items, catering_formset)
            return self.render_to_response(
                self.get_context_data(
                    catering_items=catering_items,
                    catering_formset=catering_formset,
                    catering_items_and_formset=catering_items_and_formset,
                    contact_form=contact_form))
