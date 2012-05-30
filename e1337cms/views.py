# coding: utf-8
from django.views.generic import DetailView
from django.template import Context, Template
from django.http import HttpResponse
from e1337cms.models import Page


class PageDetail(DetailView):
    model = Page
    context_object_name = 'page'

    def render_to_response(self, context, **response_kwargs):
        """
        Returns content of this page rendered with the given context.
        """
        t = Template(self.object.content)

        rendered = t.render(Context(context))
        return HttpResponse(rendered)
