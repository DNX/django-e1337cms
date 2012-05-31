from django.conf import settings
from django import template
from django.utils.encoding import smart_str, force_unicode
from django.utils.safestring import mark_safe
from django.template.base import Node
from django.template.base import Library

register = Library()


class RstNode(Node):
    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        rst_content = self.nodelist.render(context)
        try:
            from docutils.core import publish_parts
        except ImportError:
            if settings.DEBUG:
                raise template.TemplateSyntaxError("Error in 'rst' parsing: The Python docutils library isn't installed.")
            return force_unicode(rst_content)
        else:
            docutils_settings = getattr(settings, "RESTRUCTUREDTEXT_FILTER_SETTINGS", {})
            parts = publish_parts(source=smart_str(rst_content), writer_name="html4css1", settings_overrides=docutils_settings)
            return mark_safe(force_unicode(parts["html_body"]))


@register.tag
def rst(parser, token):
    """
    rst to html everything between ``{% rst %}`` and ``{% endrst %}``.

    Example usage::

        {% rst %}
            Important title
            ===============

            content...
        {% endrst %}
    """
    nodelist = parser.parse(('endrst',))
    parser.delete_first_token()
    return RstNode(nodelist)
