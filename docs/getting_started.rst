Getting Started
===============

============
Installation
============

There are a few different ways to install **e1337cms**:

Using pip
---------
If you have pip install available on your system, just type::

    pip install django-e1337cms

If you've already got an old version of **e1337cms**, and want to upgrade, use::

    pip install -U django-e1337cms

Installing from a directory
---------------------------
If you've obtained a copy of **e1337cms** using either Mercurial or a downloadable
archive, you'll need to install the copy you have system-wide. Try running::

    python setup.py develop

If that fails, you don't have ``setuptools`` or an equivalent installed;
either install them, or run::

    python setup.py install

==============================
How to use e1337cms?
==============================

If you have already installed e1337cms, you must proceed with the
configuration of your project.

Configuration
-------------
very simple, in three steps:

#. Add **e1337cms** To INSTALLED_APPS

#. Include the 'e1337cms.urls' urlpatterns at the end of your urlpatterns.

#. Optional: Modify Your settings.py, declare your **INDEX_PAGE_SLUG** and **RST_SETTINGS** settings.

Below the long explanation of each step...

Add e1337cms To INSTALLED_APPS
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
As with most Django applications, you should add **e1337cms** to the INSTALLED_APPS within your settings file (usually *settings.py*).

Example::

    INSTALLED_APPS = [
        'django.contrib.admin',
        'django.contrib.auth',
        'django.contrib.contenttypes',
        'django.contrib.sessions',
        'django.contrib.sites',

        # Added.
        'e1337cms',
    ]

Include the 'e1337cms.urls'
^^^^^^^^^^^^^^^^^^^^^^^^^^^

You need to include the 'e1337cms.urls' urlpatterns at the end of your
urlpatterns::

    url(r'^', include('e1337cms.urls')),

example::

    from django.conf.urls import patterns, include, url
    from django.contrib import admin
    admin.autodiscover()

    urlpatterns = patterns('',
        url(r'^admin/', include(admin.site.urls)),
        url(r'^', include('e1337cms.urls')),
    )

Optional: modify Your settings.py
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Within your *settings.py*, you’ll need to add some settings in order to
personalize the **e1337cms** behaviour for your project.

You can define:

- **INDEX_PAGE_SLUG** - a string, the page slug to be rendered when no another slug is passed (*default:* **'home'**)
- **RST_SETTINGS** - a dict, using this option you can pass additional settings as dictionary through the rst template block to the underlying docutils.core.publish_parts function. (*default:* **{}**)