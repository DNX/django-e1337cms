__all__ = ('VERSION',)

try:
    VERSION = __import__('pkg_resources') \
        .get_distribution('django-e1337cms').version
except Exception, e:
    VERSION = 'unknown'
