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
/testapp/author/edit/(?P<pk>\d+)/     testapp_author_update
/testapp/author/remove/(?P<pk>\d+)/   testapp_author_delete
===================================== =====================

it is also possible to add CRUD for one model::

    from django.db.models.loading import get_model
    from cruds.urls import crud_for_model
    urlpatterns += crud_for_model(get_model('testapp', 'Author'))


Quickstart
----------

Install django-cruds::

    pip install django-cruds

Then use it in a project, add ``cruds`` to ``INSTALLED_APPS``.
