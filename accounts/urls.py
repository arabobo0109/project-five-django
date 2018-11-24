from django.conf.urls import url, include
from accounts.views import index, logout, login, registration, members_home, non_members_home, about_page
from accounts import url_reset

urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', registration, name="register"),
    url(r'^members_home/$', members_home, name="members_home"),
    url(r'^about/$', about_page, name="about_page"),
    url(r'^non_members_home/$', non_members_home, name="non_members_home"),
    url(r'^password-reset/', include(url_reset)),
]