=============================
django-cruds
=============================

.. image:: https://travis-ci.org/bmihelac/django-cruds.png?branch=master
    :target: https://travis-ci.org/bmihelac/django-cruds

.. image:: https://coveralls.io/repos/bmihelac/django-cruds/badge.png?branch=master
    :target: https://coveralls.io/r/bmihelac/django-cruds?branch=master

.. image:: https://img.shields.io/pypi/v/django-cruds.svg   
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

Customizable CRUD url patterns ``crud_urls``::

    urlpatterns += crud_urls(
        Author, 
        list_view=MyAuthorListView.as_view(),
        activate=ActivateAuthorView.as_view(),
    )

Use ``cruds.util.crud_url`` shortcut function to quickly get url for
instance for given action::

    crud_url(author, 'update')

Is same as::

    reverse('testapp_author_update', kwargs={'pk': author.pk})

``cruds.util.crud_url`` accepts Model class as well for list actions, ie:

    crud_url(Author, 'list')
    crud_url(Author, 'create')

``cruds.util.crud_permission_name`` returns permission name using Django 
naming convention, ie: `testapp.change_author`.

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

* Django>=3.2<=4.0
