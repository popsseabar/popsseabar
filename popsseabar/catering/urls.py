from django.conf.urls import patterns, url

from .views import CateringView

urlpatterns = patterns(
    '',
    url(r'^$', CateringView.as_view()),
)
