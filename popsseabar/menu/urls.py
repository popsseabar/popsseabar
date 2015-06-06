from django.conf.urls import patterns, url

from .views import MenuView, SectionList, ItemList

urlpatterns = patterns(
    '',
    url(r'^$', MenuView.as_view()),
    url(r'^sections/', SectionList.as_view()),
    url(r'^items/', ItemList.as_view()),
)
