from django.conf.urls import url
from .views import search_page, do_search

urlpatterns = [
    url(r'^search_page/$', search_page, name="search_page"),
    url(r'^$', do_search, name='search')
    ]