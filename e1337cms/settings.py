from django.conf import settings

# The page slug to be rendered when no another slug is passed
INDEX_PAGE_SLUG = getattr(settings, 'INDEX_PAGE_SLUG', 'home')

# Using this option you can pass additional settings as dictionary through
# the rst template block to the underlying docutils.core.publish_parts function.
# Defaults to empty dict.
RST_SETTINGS = {}
