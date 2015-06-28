from django.conf.urls import patterns, url
from django.views.generic import TemplateView

from .views import CateringView

urlpatterns = patterns(
    '',
    url(r'^$', CateringView.as_view()),
    url(r'^success/', TemplateView.as_view(
        template_name='catering/success.html')),
)
