from django.conf.urls import url
from .views import get_content, content_detail

urlpatterns = [
    url(r'^$', get_content, name='get_content'),
    url(r'^(?P<pk>\d+)/$', content_detail, name='content_detail'),
]