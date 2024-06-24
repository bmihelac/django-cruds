# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.apps import apps

from . import utils
from .views import (
    CRUDCreateView,
    CRUDDeleteView,
    CRUDDetailView,
    CRUDListView,
    CRUDUpdateView,
)
from django.urls import re_path


def crud_urls(model,
              list_view=None,
              create_view=None,
              update_view=None,
              detail_view=None,
              delete_view=None,
              url_prefix=None,
              name_prefix=None,
              list_views=None,
              **kwargs):
    """Returns a list of url patterns for model.

    :param list_view:
    :param create_view:
    :param update_view:
    :param detail_view:
    :param delete_view:
    :param url_prefix: prefix to prepend, default is `'$'`
    :param name_prefix: prefix to prepend to name, default is empty string
    :param list_views(dict): additional list views
    :param **kwargs: additional detail views
    :returns: urls
    """
    if url_prefix is None:
        url_prefix = r'^'
    urls = []
    if list_view:
        urls.append(re_path(
            url_prefix + '$',
            list_view,
            name=utils.crud_url_name(model, utils.ACTION_LIST, name_prefix)
        ))
    if create_view:
        urls.append(re_path(
            url_prefix + r'new/$',
            create_view,
            name=utils.crud_url_name(model, utils.ACTION_CREATE, name_prefix)
        ))
    if detail_view:
        urls.append(re_path(
            url_prefix + r'(?P<pk>\d+)/$',
            detail_view,
            name=utils.crud_url_name(model, utils.ACTION_DETAIL, name_prefix)
        ))
    if update_view:
        urls.append(re_path(
            url_prefix + r'(?P<pk>\d+)/edit/$',
            update_view,
            name=utils.crud_url_name(model, utils.ACTION_UPDATE, name_prefix)
        ))
    if delete_view:
        urls.append(re_path(
            url_prefix + r'(?P<pk>\d+)/remove/$',
            delete_view,
            name=utils.crud_url_name(model, utils.ACTION_DELETE, name_prefix)
        ))

    if list_views is not None:
        for name, view in list_views.items():
            urls.append(re_path(
                url_prefix + r'%s/$' % name,
                view,
                name=utils.crud_url_name(model, name, name_prefix)
            ))

    for name, view in kwargs.items():
        urls.append(re_path(
            url_prefix + r'(?P<pk>\d+)/%s/$' % name,
            view,
            name=utils.crud_url_name(model, name, name_prefix)
        ))
    return urls


def crud_for_model(model, urlprefix=None):
    """Returns list of ``url`` items to CRUD a model.
    """
    model_lower = model.__name__.lower()

    if urlprefix is None:
        urlprefix = ''
    urlprefix += model_lower + '/'

    urls = crud_urls(
        model,
        list_view=CRUDListView.as_view(model=model),
        create_view=CRUDCreateView.as_view(model=model),
        detail_view=CRUDDetailView.as_view(model=model),
        update_view=CRUDUpdateView.as_view(model=model),
        delete_view=CRUDDeleteView.as_view(model=model),
        url_prefix=urlprefix,
    )
    return urls


def crud_for_app(app_label, urlprefix=None):
    """
    Returns list of ``url`` items to CRUD an app.
    """
    if urlprefix is None:
        urlprefix = app_label + '/'
    app = apps.get_app_config(app_label)
    urls = []
    for model in app.get_models():
        urls += crud_for_model(model, urlprefix)
    return urls
