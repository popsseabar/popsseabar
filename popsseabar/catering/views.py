from django.conf import settings
from django.core.mail import send_mail
from django.core.urlresolvers import reverse_lazy
from django.forms.models import formset_factory
from django.http import HttpResponseRedirect
from django.template.loader import render_to_string
from django.views.generic import FormView, TemplateView

from ..menu.models import Item
from .forms import CateringForm, ContactForm
from .models import Options


class CateringView(FormView):
    template_name = 'catering/index.html'
    form_class = CateringForm
    success_url = reverse_lazy('catering:success')

    options = None

    def get_options(self, options=None):
        """
        Return most recent options object
        """
        if options is None:
            # check if options exist, if not throw a 500 error
            try:
                options = Options.objects.order_by('pk').reverse()[0]
            except IndexError:
                raise Exception('Catering options not defined')
        return options

    def get(self, request):
        self.options = self.get_options()

        catering_items = Item.objects.filter(catering_active=True)\
                             .order_by('section', 'position')
        CateringFormSet = formset_factory(CateringForm, extra=catering_items.count())
        catering_formset = CateringFormSet(prefix='catering')
        catering_items_and_formset = zip(catering_items, catering_formset)
        catering_page_copy = self.options.catering_page_copy.strip()

        contact_form = ContactForm(prefix='contact')

        return self.render_to_response(
            self.get_context_data(catering_items=catering_items,
                                  catering_page_copy=catering_page_copy,
                                  catering_formset=catering_formset,
                                  catering_items_and_formset=catering_items_and_formset,
                                  contact_form=contact_form))

    def post(self, request, *args, **kwargs):
        self.options = self.get_options()

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
            html_message = render_to_string(
                'catering/email.html', message_context)

            message_context = {}
            message_context['catering_email_confirmation_copy'] = \
                self.options.catering_email_confirmation_copy.strip()
            message = render_to_string(
                'catering/email.txt', message_context)

            send_mail(
                from_email=getattr(settings, 'SERVER_EMAIL'),
                recipient_list=[self.options.catering_orders_email],
                subject='Pop\'s SeaBar Catering Order Received',
                message='',
                html_message=html_message)

            # TODO: move trimming to the model
            send_mail(
                from_email=getattr(settings, 'SERVER_EMAIL'),
                recipient_list=[cleaned_contact_form['email']],
                subject='Pop\'s SeaBar Catering Order Confirmation',
                message=message)

            return HttpResponseRedirect(self.get_success_url())

        else:
            catering_items_and_formset = zip(catering_items, catering_formset)
            return self.render_to_response(
                self.get_context_data(
                    catering_items=catering_items,
                    catering_formset=catering_formset,
                    catering_items_and_formset=catering_items_and_formset,
                    contact_form=contact_form))


class SuccessView(TemplateView):
    template_name = 'catering/success.html'

    def get_context_data(self, **kwargs):
        context = super(SuccessView, self).get_context_data(**kwargs)

        try:
            options = Options.objects.all().order_by('pk').reverse()[0]
            context['catering_email_confirmation_copy'] = \
                options.catering_email_confirmation_copy.strip()
        except IndexError:
            pass

        return context
