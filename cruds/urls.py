# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url

from . import utils
from .views import (
    CRUDCreateView,
    CRUDDeleteView,
    CRUDDetailView,
    CRUDListView,
    CRUDUpdateView,
)


def crud_for_model(model):
    """
    Returns list of ``url`` items to CRUD a model.
    """
    model_lower = model.__name__.lower()
    urls = []

    urls.append(url(
        r'%s/create/$' % model_lower,
        CRUDCreateView.as_view(model=model),
        name=utils.crud_url_name(model, utils.ACTION_CREATE)
    ))

    urls.append(url(
        r'%s/delete/(?P<pk>\d+)/$' % model_lower,
        CRUDDeleteView.as_view(model=model),
        name=utils.crud_url_name(model, utils.ACTION_DELETE)
    ))

    urls.append(url(
        r'%s/detail/(?P<pk>\d+)/$' % model_lower,
        CRUDDetailView.as_view(model=model),
        name=utils.crud_url_name(model, utils.ACTION_DETAIL)
    ))

    urls.append(url(
        r'%s/update/(?P<pk>\d+)/$' % model_lower,
        CRUDUpdateView.as_view(model=model),
        name=utils.crud_url_name(model, utils.ACTION_UPDATE)
    ))

    urls.append(url(
        r'%s/$' % model_lower,
        CRUDListView.as_view(model=model),
        name=utils.crud_url_name(model, utils.ACTION_LIST)
    ))

    return urls
