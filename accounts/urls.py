from django.conf.urls import url, include
from accounts.views import index, logout, login, registration, user_profile, members_home, non_members_home
from accounts import url_reset

urlpatterns = [
    url(r'^logout/$', logout, name="logout"),
    url(r'^login/$', login, name="login"),
    url(r'^register/$', registration, name="register"),
    url(r'^profile/$', user_profile, name="profile"),
    url(r'^members_home/$', members_home, name="members_home"),
    url(r'^non_members_home/$', non_members_home, name="non_members_home"),
    url(r'^password-reset/', include(url_reset)),
]