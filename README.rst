Some examples of content
------------------------
The content will be rendered as a django template.
The "rst" blocks will be passed to *docutils* and converted to html.

Page with rst content::

    {% load e1337tags %}
    {% rst %}
    My h1 row
    =========
    {% endrst %}
    another content, bla, <strong>blu</strong>, bli...

Page which extends a template::

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