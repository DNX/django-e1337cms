#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase
from e1337cms.models import Page


class ViewTest(TestCase):

    def setUp(self):
        self.page = Page.objects.create(title='First page title',
            slug='first-page-slug',
            content='first page content')

    def test_page_dont_exists(self):
        r = self.client.get(reverse("page", kwargs={'slug': 'dummy-slug'}))
        self.assertEquals(r.status_code, 404)

    def test_simple_page_render(self):
        r = self.client.get(reverse("page", kwargs={'slug': 'first-page-slug'}))
        self.assertContains(r, "first page content")
        self.assertNotContains(r, "First page title")
        self.page.content = '<strong>{{ page.title }}</strong>\nfirst page content'
        self.page.save()
        r = self.client.get(reverse("page", kwargs={'slug': 'first-page-slug'}))
        self.assertContains(r, "first page content")
        self.assertContains(r, "<strong>First page title</strong>")

    def test_complex_page_render(self):
        self.page.content = '''
            {% extends "base.html" %}
    {% load e1337tags %}
    {% block title %}e1337::{{ page.title }}{% endblock title %}

    {% block body %}
    {% rst %}
My h1 row
=========
    {% endrst %}
    another content, bla, <strong>blu</strong>, bli...
    <p>html content</p>

    {% endblock body %}
        '''
        self.page.save()
        r = self.client.get(reverse("page", kwargs={'slug': 'first-page-slug'}))
        self.assertContains(r, "<title>e1337::First page title</title>")
        self.assertContains(r, "<h1 class=\"title\">My h1 row</h1>")

    def test_rst_block(self):
        # title
        self.page.content = '{% load e1337tags %}{% rst %}Page title\n=================={% endrst %}'
        self.page.save()
        r = self.client.get(reverse("page", kwargs={'slug': 'first-page-slug'}))
        self.assertContains(r, "<h1 class=\"title\">Page title</h1>")
        # bold text
        self.page.content = '{% load e1337tags %}{% rst %}**bold text**{% endrst %}'
        self.page.save()
        r = self.client.get(reverse("page", kwargs={'slug': 'first-page-slug'}))
        self.assertContains(r, "<div class=\"document\">\n<p><strong>bold text</strong></p>\n</div>\n")
        # italic text
        self.page.content = '{% load e1337tags %}{% rst %}*italic text*{% endrst %}'
        self.page.save()
        r = self.client.get(reverse("page", kwargs={'slug': 'first-page-slug'}))
        self.assertContains(r, "<div class=\"document\">\n<p><em>italic text</em></p>\n</div>\n")
