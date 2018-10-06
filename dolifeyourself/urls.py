from django.conf.urls import url, include
from django.contrib import admin
from django.views import static
from django.views.generic import RedirectView
from django.views.static import serve
from accounts.views import index
from accounts import urls as accounts_urls
from ecommerce import urls as urls_products
from cart import urls as urls_cart
from checkout import urls as urls_checkout
from search import urls as urls_search
from ecommerce.views import all_products
from .settings import MEDIA_ROOT

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name="index"),
    url(r'^$', RedirectView.as_view(url='posts/')),
    url(r'posts/', include('posts.urls')), 
    url(r'^media/(?P<path>.*)$', serve, {'document_root': MEDIA_ROOT}),
    url(r'^accounts/', include(accounts_urls)),
    url(r'^products/', include(urls_products)),
    url(r'^cart/', include(urls_cart)),
    url(r'^checkout/', include(urls_checkout)),
    url(r'^search/', include(urls_search)),
]

