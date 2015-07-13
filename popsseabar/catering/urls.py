from django.conf.urls import patterns, url

from .views import CateringView, SuccessView


urlpatterns = patterns('',
    url(r'^$', CateringView.as_view(), name='index'),
    url(r'^success/', SuccessView.as_view(), name='success'),
)
