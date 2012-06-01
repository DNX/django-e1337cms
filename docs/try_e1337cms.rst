How can I try e1337cms functionality?
=====================================

#. Obtain a copy of **e1337cms** repo::

    $ hg clone ssh://hg@bitbucket.org/DNX/django-e1337cms

#. Navitate in **testsite** folder inside this repo::

    $ cd django-e1337cms/testsite/

#. Create a virtualenv::

    $ virtualenv /tmp/e1337cmsenv/

#. Activate the virtualenv::

    $ source /tmp/e1337cmsenv/bin/activate

#. Install all requirements::

    $ pip install -r requirements.txt

#. Do a **syncdb**::

    $ python manage.py syncdb

#. Migrate the db::

    $ python manage.py migrate

#. Start the server::

    $ python manage.py runserver

#. Open a browser and navigate to *http://localhost:8000*.

#. Navigate to *http://localhost:8000/admin/e1337cms/page/add/* to add some pages.