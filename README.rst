=============================
django-cruds
=============================

.. image:: https://travis-ci.org/bmihelac/django-cruds.png?branch=master
    :target: https://travis-ci.org/bmihelac/django-cruds

.. image:: https://coveralls.io/repos/bmihelac/django-cruds/badge.png?branch=master
    :target: https://coveralls.io/r/bmihelac/django-cruds?branch=master

.. image:: https://pypip.in/v/django-cruds/badge.png   
    :target: https://crate.io/packages/django-cruds

django-cruds is simple drop-in django app that creates CRUD
(Create, read, update and delete) views for existing models and apps.

django-cruds goal is to make prototyping faster.

Documentation
-------------

To add CRUD for whole app, add this to urls.py::

    from cruds.urls import crud_for_app
    urlpatterns += crud_for_app('testapp')

This will create following urls and appropriate views (assuming 
there is a application named ``testapp`` with model ``Author``:

===================================== =====================
URL                                   name
===================================== =====================
/testapp/author/                      testapp_author_list
/testapp/author/new/                  testapp_author_create
/testapp/author/(?P<pk>\d+)/          testapp_author_detail
/testapp/author/(?P<pk>\d+)/edit/     testapp_author_update
/testapp/author/(?P<pk>\d+)/remove/   testapp_author_delete
===================================== =====================

It is also possible to add CRUD for one model::

    from django.db.models.loading import get_model
    from cruds.urls import crud_for_model
    urlpatterns += crud_for_model(get_model('testapp', 'Author'))

``crud_fields`` templatetag displays fields for an object::

    {% load crud_tags %}

    <table class="table">
      <tbody>
        {% crud_fields object "name, description" %}
      </tbody>
    </table>

Templates
^^^^^^^^^

django-cruds views will append CRUD template name to a list of default
candidate template names for given action.

CRUD Templates are::

    cruds/create.html
    cruds/delete.html
    cruds/detail.html
    cruds/list.html
    cruds/update.html

Quickstart
----------

Install django-cruds::

    pip install django-cruds

Then use it in a project, add ``cruds`` to ``INSTALLED_APPS``.

Requirements
------------

* Python 2.7+ or Python 3.3+
* Django 1.4.2+
