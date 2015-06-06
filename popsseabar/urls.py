from django.conf import settings
from django.conf.urls import include, patterns, url
from django.conf.urls.static import static
from django.contrib import admin

from .views import IndexView


urlpatterns = patterns(
    '',
    url(r'^$', IndexView.as_view()),
    url(r'^menu/', include('popsseabar.menu.urls', namespace='menu')),
    url(r'^grappelli/', include('grappelli.urls')),
    url(r'^admin/', include(admin.site.urls)),

) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT, show_indexes=True)
