=============================
django-cruds
=============================

.. image:: https://travis-ci.org/bmihelac/django-cruds.png?branch=master
    :target: https://travis-ci.org/bmihelac/django-cruds

.. image:: https://coveralls.io/repos/bmihelac/django-cruds/badge.png?branch=master
    :target: https://coveralls.io/r/bmihelac/django-cruds?branch=master

django-cruds is simple drop-in django app that creates CRUD
(Create, read, update and delete) views for existing models and apps.

django-cruds goal is to make prototyping faster.

Documentation
-------------

Add CRUD for whole app, add this to urls.py::

    from cruds.urls import crud_for_app
    urlpatterns += crud_for_app('testapp')

This will create following urls and appropriate views::

    /testapp/author/
    /testapp/author/new/
    /testapp/author/(?P<pk>\d+)/
    /testapp/author/edit/(?P<pk>\d+)/
    /testapp/author/remove/(?P<pk>\d+)/

it is also possible to add CRUD for one model::

    from django.db.models.loading import get_model
    from cruds.urls import crud_for_model
    urlpatterns += crud_for_model(get_model('testapp', 'Author'))


Quickstart
----------

Install django-cruds::

    pip install django-cruds

Then use it in a project, add ``cruds`` to ``INSTALLED_APPS``.
