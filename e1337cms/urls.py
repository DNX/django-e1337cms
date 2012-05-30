from django.conf.urls.defaults import *
from e1337cms.views import PageDetail

urlpatterns = patterns('e1337cms.views',
    url(r'^(?P<slug>[0-9A-Za-z-_.//]+)/$', PageDetail.as_view(), name='page')
    )
