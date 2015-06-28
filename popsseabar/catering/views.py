import logging, pprint

from django.core.mail import send_mail
from django.forms.models import formset_factory
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.views.generic import FormView

from .forms import CateringForm, ContactForm
from ..menu.models import Item
from ..site.models import Options


logger = logging.getLogger('popsseabar')
pp = pprint.PrettyPrinter(indent=4)


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

            for item, form in cleaned_catering_items_and_formset:
                qty = form['qty']
                if qty > 0:
                    logger.debug(item.name + ' ' + str(qty))

            message_context = {}
            message_context['contact_form'] = cleaned_contact_form
            message_context['catering_items_and_formset'] = \
                cleaned_catering_items_and_formset
            order_message = render_to_string(
                'catering/email.txt', message_context)

            # 'Thank you for placing a catering order with Pop\'s SeaBar. Our staff will be contacting you shortly to confirm your order.'
            try:
                message_context['options'] = Options.objects.get(pk=1)
            except Options.DoesNotExist:
                pass
            confirmation_message = render_to_string(
                'catering/email.txt', message_context)

            send_mail(
                from_email='no-reply@popsseabar.com',
                recipient_list=['order@popsseabar.com'],
                subject='Test',
                message=order_message)

            send_mail(
                from_email='no-reply@popsseabar.com',
                recipient_list=[cleaned_contact_form['email']],
                subject='Test',
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
