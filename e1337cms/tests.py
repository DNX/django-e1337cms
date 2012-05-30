#!/usr/bin/python
# -*- coding: utf-8 -*-
from django.core.urlresolvers import reverse
from django.test import TestCase
from e1337cms.models import Page


class ViewTest(TestCase):
    def test_simple_page_render(self):
        r = self.client.get(reverse("page", kwargs={'slug': 'dummy-slug'}))
        self.assertEquals(r.status_code, 404)
        page = Page.objects.create(title='First page title',
            slug='first-page-slug',
            content='first page content')
        r = self.client.get(reverse("page", kwargs={'slug': 'first-page-slug'}))
        self.assertContains(r, "first page content")
        self.assertNotContains(r, "First page title")
        page.content = '{{ page.title }}\nfirst page content'
        page.save()
        r = self.client.get(reverse("page", kwargs={'slug': 'first-page-slug'}))
        self.assertContains(r, "first page content")
        self.assertContains(r, "First page title")
