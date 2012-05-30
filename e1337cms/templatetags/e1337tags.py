from django.template.base import Node
from django.template.base import Library

register = Library()

class RstNode(Node):
    def render(self, context):
        # TODO: convert this content to html
        return 'output html'

@register.tag
def rst(parser, token):
    """
    rst to html everything between ``{% rst %}`` and ``{% endrst %}``.
    """
    parser.skip_past('endrst')
    return RstNode()