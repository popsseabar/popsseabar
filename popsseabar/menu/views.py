# from django.shortcuts import render
from django.views.generic import ListView, TemplateView

# import pdb

from .models import Section, Item


# def detail(request, poll_id):
#     try:
#         p = Poll.objects.get(pk=poll_id)
#     except Poll.DoesNotExist:
#         raise Http404("Poll does not exist")
#     return render_to_response('polls/detail.html', {'poll': p})


class MenuView(TemplateView):
    template_name = 'menu/index.html'

    def get_context_data(self, **kwargs):
        context = super(MenuView, self).get_context_data(**kwargs)
        context['items'] = Item.objects.filter(is_active=True)\
                                       .order_by('section', 'position')
        return context


class SectionList(ListView):
    context_object_name = 'sections'

    def get_queryset(self):
        return Section.objects.all()


class ItemList(ListView):
    context_object_name = 'items'

    def get_queryset(self):
        return Item.objects.all()
