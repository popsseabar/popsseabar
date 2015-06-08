from django.views.generic import TemplateView

from .models import Options
from .menu.models import Item


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['items'] = Item.objects.filter(is_active=True)\
                                       .order_by('section', 'position')
        try:
            context['option'] = Options.objects.get(pk=1)
        except Options.DoesNotExist:
            pass

        return context
