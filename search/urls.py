from django.conf.urls import url
from .views import do_search_products

urlpatterns = [
    url(r'^$', do_search_products, name='search_products'),
    ]