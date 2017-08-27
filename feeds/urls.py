from django.conf.urls import url
from feeds.views import login_page,login_twitter, thanks, feeder

urlpatterns = [
    url(r'^$|^login/$',login_page),
    url(r'^login_twitter/$',login_twitter),
    url(r'^thanks/$',thanks),
    url(r'^feeder/$',feeder),
]

