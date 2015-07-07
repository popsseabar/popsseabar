from django.views.generic import TemplateView

from .site.models import Options
from .menu.models import Item, Image


class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['items'] = Item.objects.filter(is_active=True)\
                                       .order_by('section', 'position')

        try:
            menu = Image.objects.all().order_by('pk').reverse()[0]
            menu.aspect_ratio = '{}%'.format(menu.height / menu.width * 100)
            context['menu'] = menu
        except IndexError:
            pass

        try:
            context['options'] = Options.objects.all()\
                                                .order_by('pk').reverse()[0]
        except IndexError:
            pass

        return context
