from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin
from django.views.generic import TemplateView

from .views import IndexView

urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view()),
    url(r'^404/', TemplateView.as_view(template_name='404.html')),
    url(r'^500/', TemplateView.as_view(template_name='500.html')),
    url(r'^captcha/', include('captcha.urls')),
    url(r'^catering/', include('popsseabar.catering.urls', namespace='catering')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)
