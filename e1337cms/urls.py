from django.conf.urls.defaults import *
from e1337cms.views import PageDetail
from e1337cms import settings as e1337settings

urlpatterns = patterns('e1337cms.views',
    url(r'^(?P<slug>[0-9A-Za-z-_.//]+)/$', PageDetail.as_view(), name='page'),
    url(r'^$', PageDetail.as_view(), name='index_page', kwargs={'slug': e1337settings.INDEX_PAGE_SLUG, })
    )
